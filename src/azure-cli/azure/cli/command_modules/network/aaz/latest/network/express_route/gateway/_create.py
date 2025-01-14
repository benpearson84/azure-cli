# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network express-route gateway create",
)
class Create(AAZCommand):
    """Create an ExpressRoute gateway.

    :example: Create an ExpressRoute gateway.
        az network express-route gateway create --name MyExpressRouteGateway --resource-group MyResourceGroup --min-val 5
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/expressroutegateways/{}", "2022-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="ExpressRoute gateway name.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.location = AAZResourceLocationArg(
            help="Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.virtual_hub = AAZResourceIdArg(
            options=["--virtual-hub"],
            help="Name or ID of the virtual hub to associate with the gateway.",
            fmt=AAZResourceIdArgFormat(
                template="/subscriptions/{subscription}/resourceGroups/{resource_group}/providers/Microsoft.Network/virtualHubs/{}"
            )
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Space-separated tags: key[=value] [key[=value] ...]. Use \"\" to clear existing tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Autoscale"

        _args_schema = cls._args_schema
        _args_schema.max_val = AAZIntArg(
            options=["--max-val"],
            arg_group="Autoscale",
            help="Maximum number of scale units deployed for gateway.",
        )
        _args_schema.min_val = AAZIntArg(
            options=["--min-val"],
            arg_group="Autoscale",
            help="Minimum number of scale units deployed for gateway.  Default: 2.",
            default=2,
        )

        # define Arg Group "Properties"

        # define Arg Group "PutExpressRouteGatewayParameters"
        return cls._args_schema

    _args_sub_resource_create = None

    @classmethod
    def _build_args_sub_resource_create(cls, _schema):
        if cls._args_sub_resource_create is not None:
            _schema.id = cls._args_sub_resource_create.id
            return

        cls._args_sub_resource_create = AAZObjectArg()

        sub_resource_create = cls._args_sub_resource_create
        sub_resource_create.id = AAZStrArg(
            options=["id"],
            help="Resource ID.",
        )

        _schema.id = cls._args_sub_resource_create.id

    def _execute_operations(self):
        self.pre_operations()
        yield self.ExpressRouteGatewaysCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ExpressRouteGatewaysCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "expressRouteGatewayName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("autoScaleConfiguration", AAZObjectType)
                properties.set_prop("virtualHub", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})

            auto_scale_configuration = _builder.get(".properties.autoScaleConfiguration")
            if auto_scale_configuration is not None:
                auto_scale_configuration.set_prop("bounds", AAZObjectType)

            bounds = _builder.get(".properties.autoScaleConfiguration.bounds")
            if bounds is not None:
                bounds.set_prop("max", AAZIntType, ".max_val")
                bounds.set_prop("min", AAZIntType, ".min_val")

            virtual_hub = _builder.get(".properties.virtualHub")
            if virtual_hub is not None:
                virtual_hub.set_prop("id", AAZStrType, ".virtual_hub")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.id = AAZStrType()
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.auto_scale_configuration = AAZObjectType(
                serialized_name="autoScaleConfiguration",
            )
            properties.express_route_connections = AAZListType(
                serialized_name="expressRouteConnections",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.virtual_hub = AAZObjectType(
                serialized_name="virtualHub",
                flags={"required": True},
            )

            auto_scale_configuration = cls._schema_on_200_201.properties.auto_scale_configuration
            auto_scale_configuration.bounds = AAZObjectType()

            bounds = cls._schema_on_200_201.properties.auto_scale_configuration.bounds
            bounds.max = AAZIntType()
            bounds.min = AAZIntType()

            express_route_connections = cls._schema_on_200_201.properties.express_route_connections
            express_route_connections.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.express_route_connections.Element
            _element.id = AAZStrType()
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200_201.properties.express_route_connections.Element.properties
            properties.authorization_key = AAZStrType(
                serialized_name="authorizationKey",
            )
            properties.enable_internet_security = AAZBoolType(
                serialized_name="enableInternetSecurity",
            )
            properties.express_route_circuit_peering = AAZObjectType(
                serialized_name="expressRouteCircuitPeering",
                flags={"required": True},
            )
            properties.express_route_gateway_bypass = AAZBoolType(
                serialized_name="expressRouteGatewayBypass",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.routing_configuration = AAZObjectType(
                serialized_name="routingConfiguration",
            )
            properties.routing_weight = AAZIntType(
                serialized_name="routingWeight",
            )

            express_route_circuit_peering = cls._schema_on_200_201.properties.express_route_connections.Element.properties.express_route_circuit_peering
            express_route_circuit_peering.id = AAZStrType()

            routing_configuration = cls._schema_on_200_201.properties.express_route_connections.Element.properties.routing_configuration
            routing_configuration.associated_route_table = AAZObjectType(
                serialized_name="associatedRouteTable",
            )
            _build_schema_sub_resource_read(routing_configuration.associated_route_table)
            routing_configuration.propagated_route_tables = AAZObjectType(
                serialized_name="propagatedRouteTables",
            )
            routing_configuration.vnet_routes = AAZObjectType(
                serialized_name="vnetRoutes",
            )

            propagated_route_tables = cls._schema_on_200_201.properties.express_route_connections.Element.properties.routing_configuration.propagated_route_tables
            propagated_route_tables.ids = AAZListType()
            propagated_route_tables.labels = AAZListType()

            ids = cls._schema_on_200_201.properties.express_route_connections.Element.properties.routing_configuration.propagated_route_tables.ids
            ids.Element = AAZObjectType()
            _build_schema_sub_resource_read(ids.Element)

            labels = cls._schema_on_200_201.properties.express_route_connections.Element.properties.routing_configuration.propagated_route_tables.labels
            labels.Element = AAZStrType()

            vnet_routes = cls._schema_on_200_201.properties.express_route_connections.Element.properties.routing_configuration.vnet_routes
            vnet_routes.bgp_connections = AAZListType(
                serialized_name="bgpConnections",
                flags={"read_only": True},
            )
            vnet_routes.static_routes = AAZListType(
                serialized_name="staticRoutes",
            )

            bgp_connections = cls._schema_on_200_201.properties.express_route_connections.Element.properties.routing_configuration.vnet_routes.bgp_connections
            bgp_connections.Element = AAZObjectType()
            _build_schema_sub_resource_read(bgp_connections.Element)

            static_routes = cls._schema_on_200_201.properties.express_route_connections.Element.properties.routing_configuration.vnet_routes.static_routes
            static_routes.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.express_route_connections.Element.properties.routing_configuration.vnet_routes.static_routes.Element
            _element.address_prefixes = AAZListType(
                serialized_name="addressPrefixes",
            )
            _element.name = AAZStrType()
            _element.next_hop_ip_address = AAZStrType(
                serialized_name="nextHopIpAddress",
            )

            address_prefixes = cls._schema_on_200_201.properties.express_route_connections.Element.properties.routing_configuration.vnet_routes.static_routes.Element.address_prefixes
            address_prefixes.Element = AAZStrType()

            virtual_hub = cls._schema_on_200_201.properties.virtual_hub
            virtual_hub.id = AAZStrType()

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


def _build_schema_sub_resource_create(_builder):
    if _builder is None:
        return
    _builder.set_prop("id", AAZStrType, ".id")


_schema_sub_resource_read = None


def _build_schema_sub_resource_read(_schema):
    global _schema_sub_resource_read
    if _schema_sub_resource_read is not None:
        _schema.id = _schema_sub_resource_read.id
        return

    _schema_sub_resource_read = AAZObjectType()

    sub_resource_read = _schema_sub_resource_read
    sub_resource_read.id = AAZStrType()

    _schema.id = _schema_sub_resource_read.id


__all__ = ["Create"]
