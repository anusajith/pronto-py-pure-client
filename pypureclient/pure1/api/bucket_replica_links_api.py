# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six
from typing import List, Optional

from .. import models


class BucketReplicaLinksApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api10_bucket_replica_links_get_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        continuation_token=None,  # type: str
        filter=None,  # type: str
        ids=None,  # type: List[str]
        limit=None,  # type: int
        member_ids=None,  # type: List[str]
        member_names=None,  # type: List[str]
        offset=None,  # type: int
        sort=None,  # type: List[str]
        source_ids=None,  # type: List[str]
        source_names=None,  # type: List[str]
        target_ids=None,  # type: List[str]
        target_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.BucketReplicaLinkGetResponse
        """Get bucket replica links

        Retrieves information about bucket replica links. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api10_bucket_replica_links_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param list[str] ids: A comma-separated list of resource IDs. If there is not at least one resource that matches each of the elements of ids, an error is returned. Single quotes are required around all strings.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param list[str] member_ids: A list of member IDs. Member IDs separated by a `+` indicate that both members must be present in each element. Member IDs separated by a `,` indicate that at least one member must be present in each element. If there is not at least one member that matches each of the elements of `member_ids`, an error is returned. Single quotes are required around all strings. When using Try it Out in Swagger, a list of member IDs separated by a `+` must be entered in the same item cell.
        :param list[str] member_names: A list of member names. Member names separated by a `+` indicate that both members must be present in each element. Member names separated by a `,` indicate that at least one member must be present in each element. If there is not at least one member that matches each of the elements of `member_ids`, an error is returned. Single quotes are required around all strings. When using Try it Out in Swagger, a list of member names separated by a `+` must be entered in the same item cell.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :param list[str] source_ids: A list of source IDs. Source IDs separated by a `+` indicate that both sources must be present in each element. Source IDs separated by a `,` indicate that at least one source must be present in each element. If there is not at least one source that matches each of the elements of `source_ids`, an error is returned. Single quotes are required around all strings. When using Try it Out in Swagger, a list of source IDs separated by a `+` must be entered in the same item cell.
        :param list[str] source_names: A list of source names. Source names separated by a `+` indicate that both sources must be present in each element. Source names separated by a `,` indicate that at least one source must be present in each element. If there is not at least one source that matches each of the elements of `source_ids`, an error is returned. Single quotes are required around all strings. When using Try it Out in Swagger, a list of source names separated by a `+` must be entered in the same item cell.
        :param list[str] target_ids: A list of target IDs. Target IDs separated by a `+` indicate that both targets must be present in each element. Target IDs separated by a `,` indicate that at least one target must be present in each element. If there is not at least one target that matches each of the elements of `target_ids`, an error is returned. Single quotes are required around all strings. When using Try it Out in Swagger, a list of target IDs separated by a `+` must be entered in the same item cell.
        :param list[str] target_names: A list of target names. Target names separated by a `+` indicate that both targets must be present in each element. Target names separated by a `,` indicate that at least one target must be present in each element. If there is not at least one target that matches each of the elements of `target_ids`, an error is returned. Single quotes are required around all strings. When using Try it Out in Swagger, a list of target names separated by a `+` must be entered in the same item cell.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: BucketReplicaLinkGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api10_bucket_replica_links_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'member_ids' in params:
            query_params.append(('member_ids', params['member_ids']))
            collection_formats['member_ids'] = 'csv'
        if 'member_names' in params:
            query_params.append(('member_names', params['member_names']))
            collection_formats['member_names'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'
        if 'source_ids' in params:
            query_params.append(('source_ids', params['source_ids']))
            collection_formats['source_ids'] = 'csv'
        if 'source_names' in params:
            query_params.append(('source_names', params['source_names']))
            collection_formats['source_names'] = 'csv'
        if 'target_ids' in params:
            query_params.append(('target_ids', params['target_ids']))
            collection_formats['target_ids'] = 'csv'
        if 'target_names' in params:
            query_params.append(('target_names', params['target_names']))
            collection_formats['target_names'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/1.0/bucket-replica-links', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BucketReplicaLinkGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )
