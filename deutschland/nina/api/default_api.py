"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.nina.api_client import ApiClient, Endpoint as _Endpoint
from deutschland.nina.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from deutschland.nina.model.ags_covid_rules import AGSCovidRules
from deutschland.nina.model.ags_overview_result import AGSOverviewResult
from deutschland.nina.model.map_warnings import MapWarnings


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.appdata_covid_covidrules_deags_json_get_endpoint = _Endpoint(
            settings={
                "response_type": (AGSCovidRules,),
                "auth": [],
                "endpoint_path": "/appdata/covid/covidrules/DE/{AGS}.json",
                "operation_id": "appdata_covid_covidrules_deags_json_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "ags",
                ],
                "required": [
                    "ags",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "ags": (str,),
                },
                "attribute_map": {
                    "ags": "AGS",
                },
                "location_map": {
                    "ags": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.biwapp_map_data_json_get_endpoint = _Endpoint(
            settings={
                "response_type": (MapWarnings,),
                "auth": [],
                "endpoint_path": "/biwapp/mapData.json",
                "operation_id": "biwapp_map_data_json_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.dashboard_ags_json_get_endpoint = _Endpoint(
            settings={
                "response_type": (AGSOverviewResult,),
                "auth": [],
                "endpoint_path": "/dashboard/{AGS}.json",
                "operation_id": "dashboard_ags_json_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "ags",
                ],
                "required": [
                    "ags",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "ags": (str,),
                },
                "attribute_map": {
                    "ags": "AGS",
                },
                "location_map": {
                    "ags": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.katwarn_map_data_json_get_endpoint = _Endpoint(
            settings={
                "response_type": (MapWarnings,),
                "auth": [],
                "endpoint_path": "/katwarn/mapData.json",
                "operation_id": "katwarn_map_data_json_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.mowas_map_data_json_get_endpoint = _Endpoint(
            settings={
                "response_type": (MapWarnings,),
                "auth": [],
                "endpoint_path": "/mowas/mapData.json",
                "operation_id": "mowas_map_data_json_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def appdata_covid_covidrules_deags_json_get(self, ags, **kwargs):
        """Corona Regelungen nach AGS  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.appdata_covid_covidrules_deags_json_get(ags, async_req=True)
        >>> result = thread.get()

        Args:
            ags (str): Amtlicher Gebietsschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AGSCovidRules
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["ags"] = ags
        return (
            self.appdata_covid_covidrules_deags_json_get_endpoint.call_with_http_info(
                **kwargs
            )
        )

    def biwapp_map_data_json_get(self, **kwargs):
        """Biwapp Meldungen  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.biwapp_map_data_json_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MapWarnings
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.biwapp_map_data_json_get_endpoint.call_with_http_info(**kwargs)

    def dashboard_ags_json_get(self, ags, **kwargs):
        """Meldungsübersicht nach AGS  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.dashboard_ags_json_get(ags, async_req=True)
        >>> result = thread.get()

        Args:
            ags (str): Amtlicher Gebietsschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden. Die Letzten 7 Stellen müssen dabei mit \"0000000\" ersetzt werden, weil die Daten nur auf [Kreisebene](https://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel) bereitgestellt werden.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AGSOverviewResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["ags"] = ags
        return self.dashboard_ags_json_get_endpoint.call_with_http_info(**kwargs)

    def katwarn_map_data_json_get(self, **kwargs):
        """Katwarn Meldungen  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.katwarn_map_data_json_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MapWarnings
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.katwarn_map_data_json_get_endpoint.call_with_http_info(**kwargs)

    def mowas_map_data_json_get(self, **kwargs):
        """Mowas Meldungen  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mowas_map_data_json_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MapWarnings
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.mowas_map_data_json_get_endpoint.call_with_http_info(**kwargs)