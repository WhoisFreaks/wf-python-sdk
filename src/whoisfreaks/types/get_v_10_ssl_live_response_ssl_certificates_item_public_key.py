# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetV10SslLiveResponseSslCertificatesItemPublicKey(UniversalBaseModel):
    key_size: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="keySize")] = None
    key_algorithm: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="keyAlgorithm")] = None
    pem_raw: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="pemRaw")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
