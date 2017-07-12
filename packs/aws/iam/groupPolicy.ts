// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";

export class GroupPolicy extends lumi.NamedResource implements GroupPolicyArgs {
    public readonly group: string;
    public readonly _name?: string;
    public readonly namePrefix?: string;
    public readonly policy: string;

    constructor(name: string, args: GroupPolicyArgs) {
        super(name);
        this.group = args.group;
        this._name = args._name;
        this.namePrefix = args.namePrefix;
        this.policy = args.policy;
    }
}

export interface GroupPolicyArgs {
    readonly group: string;
    readonly _name?: string;
    readonly namePrefix?: string;
    readonly policy: string;
}
