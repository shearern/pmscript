
from abc import ABCMeta, abstractmethod, abstractproperty

from .exceptions import RequestError, RestAttributeMissing

class ChildRestObjectCollection: pass


class RestObject(metaclass=ABCMeta):
    '''
    Base object for access the ProcessMaker API

    Rest Objects represent records in the remote system that are retrievable through a REST
    API.  This object transparrently handles the REST calls to make the records and attributes
    available.

    '''

    UID_ONLY=1
    LIST_LVL=2
    DETAIL_LVL=3

    CHILD_CLASSES = ChildRestObjectCollection()    # Populated by __init__.py

    OBJ_CACHE = dict()  # [class_name][uid] = RestObject

    def __init__(self, rif, uid, data=None, data_level=1):
        '''
        Object data can normally be retrieved in 3 ways:

            UID_ONLY    -> Object UID is lested somewhere, but no details
            LIST_LVL    -> Some (but not all) object attributes are returned in a list
            DETAIL_LVL  -> All attributes of the object have been returned.  Typically by requesting
                           detail for a record.

        :param rif: RestIF for using the ProcessMaker REST API
        :param uid: Unique ID of this object
        :param data: Data
        :param data_level:
        '''
        self.rif = rif
        self.uid = uid
        self.data = data
        self.__data_level = data_level

        # Sanity Check: Data provided?
        if self.__data_level != self.UID_ONLY and self.data is None:
            raise Exception("Level provided, but no data")

        # Make sure data is a dict, since coming from REST API responses
        try:
            assert self.data is None or self.data.__class__ is dict
        except:
            raise Exception("Data provided is %s, but needs to be a dict" % (
                self.data.__class__.__name__))


    @property
    def data_level_desc(self):
        if self.__data_level == 1:
            return "UID_ONLY"
        elif self.__data_level == 2:
            return "LIST_DATA"
        elif self.__data_level == 3:
            return "DETAIL_DATA"
        else:
            raise Exception("Invalid data level: " + str(self.__data_level))


    def _rest_obj_attr(self, level, key, optional=False, default=None, alt=None):
        '''
        Get a attribute value

        :param level: The level the retrieval granularity level that is needed to get this attribute
        :param key: The data key
        :param alt: Alternate data keys
        '''

        if self.__data_level < level:
            self._retireve_obj_detail()

        try:
            return self.data[key]
        except KeyError:

            # Try alt keys
            if alt is not None:
                for alt_key in alt:
                    try:
                        return self.data[alt_key]
                    except KeyError:
                        pass

            # Handle key is missing error
            if optional:
                return default
            else:
                raise RestAttributeMissing(
                    "Data for %s at level %s doesn't have key %s.\nKeys are: %s" % (
                    self.__class__.__name__,
                    self.data_level_desc,
                    key,
                    ', '.join(sorted(self.data.keys()))))


    def _retireve_obj_detail(self):
        '''
        Get object detail from REST API

        Most objects can be retireved by a GET to a url, so that is the default implementation
        and we just need to know the _detail_url()
        '''
        url = self._detail_url()
        data = self.rif.get(url)

        # Make sure data is a dict, since coming from REST API responses
        try:
            assert data is None or data.__class__ is dict
        except:
            raise Exception("Data provided is %s, but needs to be a dict" % (
                data.__class__.__name__))

        # Make sure we got the correct UID
        if self._uid_key is not None:
            try:
                uid = data[self._uid_key]
                if uid != self.uid:
                    raise RequestError("Requested %s UID %s from %s, but got UID %s" % (
                        self.__class__.__name__,
                        self.uid,
                        url,
                        data[self._uid_key]))
            except KeyError:
                raise RequestError("Requested %s detail from %s, but UID key %s doesn't exist in data.\nKeys are: %s" % (
                    self.__class__.__name__,
                    url,
                    self._uid_key,
                    ', '.join(sorted(self.data.keys())),
                ))

        self.data = data
        self.__data_level = self.DETAIL_LVL


    def _detail_url(self):
        '''URL to retrieve detail for this object'''
        raise NotImplementedError("Need to define _detail_url() or _retireve_obj_detail() for %s" % (
            self.__class__.__name__))


    @abstractproperty
    def _uid_key(self):
        '''The data key that stores the object UID'''


    def _assoc_rest_obj(self, obj_class_name, uid, no_cache=False):
        '''Return a reference to an associated REST object'''

        assert(not obj_class_name.startswith('_'))

        # Return from cache if we can
        if not no_cache:
            try:
                return RestObject.OBJ_CACHE[obj_class_name][uid]
            except KeyError:
                pass

        # Create a new object
        try:
            cls = getattr(self.CHILD_CLASSES, obj_class_name)
        except:
            raise Exception("No child class defined for '%s' in CHILD_CLASSES.  Check __init__.py" % (
                obj_class_name
            ))
        obj = cls(self.rif, uid=uid)

        # Cache
        try:
            RestObject.OBJ_CACHE[obj_class_name][uid] = obj
        except KeyError:
            RestObject.OBJ_CACHE[obj_class_name] = dict()
            RestObject.OBJ_CACHE[obj_class_name][uid] = obj

        return obj
