# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from ... import utilities, tables


class PodDisruptionBudgetList(pulumi.CustomResource):
    api_version: pulumi.Output[str]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    items: pulumi.Output[list]
    kind: pulumi.Output[str]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: pulumi.Output[dict]
    def __init__(__self__, resource_name, opts=None, api_version=None, items=None, kind=None, metadata=None, __props__=None, __name__=None, __opts__=None):
        """
        PodDisruptionBudgetList is a collection of PodDisruptionBudgets.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

        The **items** object supports the following:

          * `api_version` (`pulumi.Input[str]`) - APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
          * `kind` (`pulumi.Input[str]`) - Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
          * `metadata` (`pulumi.Input[dict]`)
            * `annotations` (`pulumi.Input[dict]`) - Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations
            * `cluster_name` (`pulumi.Input[str]`) - The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.
            * `creation_timestamp` (`pulumi.Input[str]`) - CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.
              
              Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
            * `deletion_grace_period_seconds` (`pulumi.Input[float]`) - Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.
            * `deletion_timestamp` (`pulumi.Input[str]`) - DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.
              
              Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
            * `finalizers` (`pulumi.Input[list]`) - Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.
            * `generate_name` (`pulumi.Input[str]`) - GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.
              
              If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).
              
              Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency
            * `generation` (`pulumi.Input[float]`) - A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.
            * `labels` (`pulumi.Input[dict]`) - Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels
            * `managed_fields` (`pulumi.Input[list]`) - ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.
              * `api_version` (`pulumi.Input[str]`) - APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.
              * `fieldsType` (`pulumi.Input[str]`) - FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"
              * `fieldsV1` (`pulumi.Input[dict]`) - FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.
              * `manager` (`pulumi.Input[str]`) - Manager is an identifier of the workflow managing these fields.
              * `operation` (`pulumi.Input[str]`) - Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.
              * `time` (`pulumi.Input[str]`) - Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'

            * `name` (`pulumi.Input[str]`) - Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names
            * `namespace` (`pulumi.Input[str]`) - Namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.
              
              Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces
            * `owner_references` (`pulumi.Input[list]`) - List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.
              * `api_version` (`pulumi.Input[str]`) - API version of the referent.
              * `blockOwnerDeletion` (`pulumi.Input[bool]`) - If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.
              * `controller` (`pulumi.Input[bool]`) - If true, this reference points to the managing controller.
              * `kind` (`pulumi.Input[str]`) - Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
              * `name` (`pulumi.Input[str]`) - Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names
              * `uid` (`pulumi.Input[str]`) - UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids

            * `resource_version` (`pulumi.Input[str]`) - An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.
              
              Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
            * `self_link` (`pulumi.Input[str]`) - SelfLink is a URL representing this object. Populated by the system. Read-only.
              
              DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.
            * `uid` (`pulumi.Input[str]`) - UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.
              
              Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids

          * `spec` (`pulumi.Input[dict]`) - Specification of the desired behavior of the PodDisruptionBudget.
            * `max_unavailable` (`pulumi.Input[dict]`) - An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with "minAvailable".
            * `min_available` (`pulumi.Input[dict]`) - An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying "100%".
            * `selector` (`pulumi.Input[dict]`) - Label query over pods whose evictions are managed by the disruption budget.
              * `match_expressions` (`pulumi.Input[list]`) - matchExpressions is a list of label selector requirements. The requirements are ANDed.
                * `key` (`pulumi.Input[str]`) - key is the label key that the selector applies to.
                * `operator` (`pulumi.Input[str]`) - operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
                * `values` (`pulumi.Input[list]`) - values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

              * `match_labels` (`pulumi.Input[dict]`) - matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

          * `status` (`pulumi.Input[dict]`) - Most recently observed status of the PodDisruptionBudget.
            * `current_healthy` (`pulumi.Input[float]`) - current number of healthy pods
            * `desired_healthy` (`pulumi.Input[float]`) - minimum desired number of healthy pods
            * `disrupted_pods` (`pulumi.Input[dict]`) - DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn't occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions.
            * `disruptions_allowed` (`pulumi.Input[float]`) - Number of pod disruptions that are currently allowed.
            * `expected_pods` (`pulumi.Input[float]`) - total number of pods counted by this disruption budget
            * `observed_generation` (`pulumi.Input[float]`) - Most recent generation observed when updating this PDB status. DisruptionsAllowed and other status information is valid only if observedGeneration equals to PDB's object generation.

        The **metadata** object supports the following:

          * `continue_` (`pulumi.Input[str]`) - continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.
          * `remaining_item_count` (`pulumi.Input[float]`) - remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.
          * `resource_version` (`pulumi.Input[str]`) - String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
          * `self_link` (`pulumi.Input[str]`) - selfLink is a URL representing this object. Populated by the system. Read-only.
            
            DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['api_version'] = api_version
            if items is None:
                raise TypeError("Missing required property 'items'")
            __props__['items'] = items
            __props__['kind'] = kind
            __props__['metadata'] = metadata
        super(PodDisruptionBudgetList, __self__).__init__(
            'kubernetes:policy/v1beta1:PodDisruptionBudgetList',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None):
        """
        Get an existing PodDisruptionBudgetList resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        return PodDisruptionBudgetList(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
