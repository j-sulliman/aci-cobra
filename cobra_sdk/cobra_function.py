def apic_logon(apic_url='https://sample-host.coolapi.com', user="admin",
    password="password"):

    import cobra.mit.access
    import cobra.mit.request
    import cobra.mit.session

    ls = cobra.mit.session.LoginSession(apic_url, user, password)
    md = cobra.mit.access.MoDirectory(ls)
    md.login()


    return md


def create_tenant(logon_session, tenant_name="Example_TN", description="Description"):

    from cobra.internal.codec.jsoncodec import toJSONStr
    from cobra.model.fv import Tenant, RsTenantMonPol
    from cobra.mit.request import ConfigRequest
    import cobra.model.pol
    import cobra.model.vns
    c = ConfigRequest()
    #apic_logon(apic_url, user, password)
    polUni = cobra.model.pol.Uni('')

    fvTenant = Tenant(polUni, ownerKey=u'', name=tenant_name,
        descr=description, nameAlias=tenant_name, ownerTag=u'', annotation=u'')
    vnsSvcCont = cobra.model.vns.SvcCont(fvTenant, annotation=u'')
    fvRsTenantMonPol = RsTenantMonPol(fvTenant, annotation=u'',
        tnMonEPGPolName=u'')

    tenant_data = toJSONStr(polUni)

    c.addMo(polUni)
    logon_session.commit(c)
    return tenant_data

def create_apn(logon_session, tenant_name="Example_TN",
    description="Description", ap_name=''):

    from cobra.internal.codec.jsoncodec import toJSONStr
    from cobra.model.fv import Tenant, RsTenantMonPol, Ap
    from cobra.mit.request import ConfigRequest
    import cobra.model.pol
    import cobra.model.vns
    c = ConfigRequest()
    #apic_logon(apic_url, user, password)
    polUni = cobra.model.pol.Uni('')

    fvTenant = Tenant(polUni, tenant_name)

    # build the request using cobra syntax
    fvAp = Ap(fvTenant, ownerKey=u'', name=ap_name, descr=description,
    nameAlias=u'', ownerTag=u'', prio=u'unspecified', annotation=u'')


    apn_data = toJSONStr(polUni)

    c.addMo(polUni)
    logon_session.commit(c)
    return apn_data

def create_vrf(logon_session, tenant_name="Example_TN",
    description="Description", vrf_name=''):

    from cobra.internal.codec.jsoncodec import toJSONStr
    from cobra.model.fv import Tenant, RsTenantMonPol, Ctx, RsOspfCtxPol
    from cobra.model.fv import RsCtxToExtRouteTagPol, RsBgpCtxPol, RsCtxToEpRet
    from cobra.model.fv import RsBgpCtxPol, RsVrfValidationPol
    from cobra.mit.request import ConfigRequest
    import cobra.model.pol
    import cobra.model.vns
    from cobra.model.vz import Any
    c = ConfigRequest()
    #apic_logon(apic_url, user, password)
    polUni = cobra.model.pol.Uni('')

    fvTenant = Tenant(polUni, tenant_name)

    fvCtx = Ctx(fvTenant, ownerKey=u'', name=vrf_name,
        descr=u'', knwMcastAct=u'permit', pcEnfDir=u'ingress', nameAlias=u'',
        ownerTag=u'', annotation=u'', pcEnfPref=u'enforced',
        bdEnforcedEnable=u'no')
    fvRsVrfValidationPol = RsVrfValidationPol(fvCtx,
        tnL3extVrfValidationPolName=u'', annotation=u'')
    vzAny = Any(fvCtx, matchT=u'AtleastOne', name=u'', descr=u'',
        prefGrMemb=u'disabled', nameAlias=u'', annotation=u'')
    fvRsOspfCtxPol = RsOspfCtxPol(fvCtx, annotation=u'',
        tnOspfCtxPolName=u'')
    fvRsCtxToEpRet = RsCtxToEpRet(fvCtx, annotation=u'',
    tnFvEpRetPolName=u'')
    fvRsCtxToExtRouteTagPol = RsCtxToExtRouteTagPol(fvCtx,
        annotation=u'', tnL3extRouteTagPolName=u'')
    fvRsBgpCtxPol = RsBgpCtxPol(fvCtx,
        tnBgpCtxPolName=u'', annotation=u'')

    ctx_data = toJSONStr(polUni)

    c.addMo(polUni)
    logon_session.commit(c)
    return ctx_data

def create_epg(logon_session, tenant_name="Example_TN",
    description="Description", ap_name='', epg_name='', vpc_leaf_1 = '101',
    vpc_leaf_2 = '102', int_pol='', vlan_encap='', phy_dom='', bd=''):

    from cobra.internal.codec.jsoncodec import toJSONStr
    from cobra.model.fv import Tenant, RsTenantMonPol, Ap
    from cobra.mit.request import ConfigRequest
    import cobra.model.pol
    import cobra.model.vns
    c = ConfigRequest()
    #apic_logon(apic_url, user, password)
    polUni = cobra.model.pol.Uni('')

    fvTenant = Tenant(polUni, tenant_name)
    fvAp = cobra.model.fv.Ap(fvTenant, ap_name)

    # build the request using cobra syntax
    fvAEPg = cobra.model.fv.AEPg(fvAp, isAttrBasedEPg=u'no',
        matchT=u'AtleastOne', name=epg_name, descr=u'',
        fwdCtrl=u'', prefGrMemb=u'exclude', exceptionTag=u'',
        floodOnEncap=u'disabled', nameAlias=u'', prio=u'unspecified',
        annotation=u'', pcEnfPref=u'unenforced')
    fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg,
        tDn=u'topology/pod-1/protpaths-{}-{}/pathep-[{}]'.format(vpc_leaf_1,
        vpc_leaf_2, vpc_leaf_1, vpc_leaf_2, int_pol, phy_dom),
        descr=u'', primaryEncap=u'unknown', instrImedcy=u'lazy',
        mode=u'regular', encap=u'vlan-{}'.format(vlan_encap), annotation=u'')
    fvRsDomAtt = cobra.model.fv.RsDomAtt(fvAEPg,
        tDn=u'uni/phys-{}'.format(phy_dom),
        netflowDir=u'both', epgCos=u'Cos0', classPref=u'encap',
        netflowPref=u'disabled', secondaryEncapInner=u'unknown',
        resImedcy=u'immediate', delimiter=u'', instrImedcy=u'lazy',
        primaryEncapInner=u'unknown', encap=u'unknown', switchingMode=u'native',
        primaryEncap=u'unknown', encapMode=u'auto', annotation=u'',
        epgCosPref=u'disabled')
    fvRsCustQosPol = cobra.model.fv.RsCustQosPol(fvAEPg, annotation=u'',
        tnQosCustomPolName=u'')
    fvRsBd = cobra.model.fv.RsBd(fvAEPg, annotation=u'',
        tnFvBDName=bd)


    epg_data = toJSONStr(polUni)

    c.addMo(polUni)
    logon_session.commit(c)
    return epg_data

def create_bd(logon_session, tenant_name="Example_TN",
    description="Description", bd_name='', vrf_name=''):

    from cobra.internal.codec.jsoncodec import toJSONStr
    from cobra.model.fv import Tenant, RsTenantMonPol, BD, RsIgmpsn, RsCtx
    from cobra.model.fv import RsBdToEpRet, RsBDToNdP
    from cobra.mit.request import ConfigRequest
    import cobra.model.pol
    import cobra.model.vns
    c = ConfigRequest()
    #apic_logon(apic_url, user, password)
    polUni = cobra.model.pol.Uni('')

    fvTenant = Tenant(polUni, tenant_name)

    fvBD = BD(fvTenant, multiDstPktAct=u'bd-flood', mcastAllow=u'no',
        limitIpLearnToSubnets=u'yes', unicastRoute=u'no', unkMcastAct=u'flood',
        descr=u'', llAddr=u'::', nameAlias=u'', type=u'regular',
        ipLearning=u'no', vmac=u'not-applicable', mac=u'00:22:BD:F8:19:FF',
        epMoveDetectMode=u'', ownerTag=u'', intersiteBumTrafficAllow=u'no',
        annotation=u'', ownerKey=u'', name=bd_name, epClear=u'no',
        unkMacUcastAct=u'flood', arpFlood=u'yes', intersiteL2Stretch=u'no',
        OptimizeWanBandwidth=u'no')
    fvRsIgmpsn = RsIgmpsn(fvBD, tnIgmpSnoopPolName=u'', annotation=u'')
    fvRsCtx = RsCtx(fvBD, annotation=u'', tnFvCtxName=vrf_name)
    fvRsBdToEpRet = RsBdToEpRet(fvBD, resolveAct=u'resolve', annotation=u'',
        tnFvEpRetPolName=u'')
    fvRsBDToNdP = RsBDToNdP(fvBD, annotation=u'', tnNdIfPolName=u'')


    bd_data = toJSONStr(polUni)

    c.addMo(polUni)
    logon_session.commit(c)
    return bd_data
