import sys
from collections.abc import Iterator, Mapping, Sequence
from typing import Any, NewType, Optional, TypeVar, overload

if sys.version_info < (3, 12):
    from typing_extensions import Buffer
else:
    from collections.abc import Buffer

if sys.version_info < (3, 11):
    from typing_extensions import Self
else:
    from typing import Self

TNSObject = TypeVar("TNSObject", bound=NSObject)

class NSObject:
    @classmethod
    def alloc(cls) -> Self: ...
    def init(self) -> Optional[Self]: ...
    def addObserver_forKeyPath_options_context_(
        self,
        observer: NSObject,
        keyPath: str,
        options: NSKeyValueObservingOptions,
        context: int,
    ) -> None: ...
    def removeObserver_forKeyPath_(self, observer: NSObject, keyPath: str) -> None: ...

class NSDictionary(NSObject, Mapping[str, Any]):
    def __getitem__(self, key: str) -> Any: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...

class NSUUID(NSObject):
    @classmethod
    def UUIDWithString_(cls, uuidString: str) -> NSUUID: ...
    def UUIDString(self) -> str: ...
    def isEqualToUUID_(self, other: NSUUID) -> bool: ...

class NSError(NSObject): ...

class NSData(NSObject, Buffer):
    def initWithBytes_length_(self, bytes: Buffer, length: int) -> Self: ...
    def length(self) -> int: ...
    def getBytes_length_(self, buffer: bytes, length: int) -> None: ...

T = TypeVar("T")

class NSArray(NSObject, Sequence[T]):
    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __len__(self) -> int: ...
    def initWithArray_(self, array: Sequence[Any]) -> Self: ...

class NSValue(NSObject): ...

class NSBundle(NSObject):
    @classmethod
    def mainBundle(cls) -> NSBundle: ...
    def bundleIdentifier(self) -> str: ...

NSKeyValueObservingOptions = NewType("NSKeyValueObservingOptions", int)
NSKeyValueObservingOptionNew: NSKeyValueObservingOptions
NSKeyValueObservingOptionOld: NSKeyValueObservingOptions
NSKeyValueObservingOptionInitial: NSKeyValueObservingOptions
NSKeyValueObservingOptionPrior: NSKeyValueObservingOptions

NSKeyValueChangeKey = NewType("NSKeyValueChangeKey", str)
NSKeyValueChangeIndexesKey: NSKeyValueChangeKey
NSKeyValueChangeKindKey: NSKeyValueChangeKey
NSKeyValueChangeNewKey: NSKeyValueChangeKey
NSKeyValueChangeNotificationIsPriorKey: NSKeyValueChangeKey
NSKeyValueChangeOldKey: NSKeyValueChangeKey
