from cobra_sdk.cobra_function import apic_logon, create_tenant, create_apn
from cobra_sdk.cobra_function import create_epg, create_bd, create_vrf
import pandas as pd

def main():
    logfile = open("Tenant-Configuration.log", "w+")
    legacy_vlans = pd.read_excel(open('spreadsheet/ASB-LEGACY-VLAN_Workbook.xlsx',
     'rb'),sheet_name='Sheet1')
     # edit as required
    session = apic_logon(apic_url="https://10.37.1.11", user="admin",
        password="dr1ft3r*")

    tenant_lst = []
    app_profile_lst = []
    vrf_lst = []
    epg_lst = []
    bd_list = []
    for index, row in legacy_vlans.iterrows():
        if row["PROPOSED_TENANT"] not in tenant_lst:
            tenant = create_tenant(session, tenant_name=row["PROPOSED_TENANT"],
                description=row["PROPOSED_DESCRIPTION"])
            tenant_lst.append(row["PROPOSED_TENANT"])
            logfile.write(tenant)
            logfile.write("\n\n")
            print(tenant)
        if row["VRF"] not in vrf_lst:
            vrf = create_vrf(session, tenant_name=row["PROPOSED_TENANT"],
                description=row["PROPOSED_DESCRIPTION"],
                vrf_name=row['PROPOSED_VRF'])
            vrf_lst.append(row["VRF"])
            logfile.write(vrf)
            logfile.write("\n\n")
            print(vrf)
        if row["PROPOSED_APP_PROFILE"] not in app_profile_lst:
            app_prof = create_apn(session, tenant_name=row["PROPOSED_TENANT"],
                description=row["PROPOSED_DESCRIPTION"],
                ap_name=row['PROPOSED_APP_PROFILE'])
            app_profile_lst.append(row["PROPOSED_APP_PROFILE"])
            logfile.write(app_prof)
            logfile.write("\n\n")
            print(app_prof)
        if row["VLAN_ID"] not in epg_lst:
            epg = create_epg(session,
                tenant_name=row["PROPOSED_TENANT"],
                description=row["PROPOSED_DESCRIPTION"],
                ap_name=row['PROPOSED_APP_PROFILE'],
                epg_name=row['PROPOSED_EPG'],
                vpc_leaf_1 = '101',
                vpc_leaf_2 = '102',
                int_pol=row['PROPOSED_IPG'],
                vlan_encap=row['VLAN_ID'],
                phy_dom=row['PROPOSED_PHYDOM'],
                bd=row['PROPOSED_BD'])
            bridge_domain = create_bd(session,
                tenant_name=row["PROPOSED_TENANT"],
                description=row["PROPOSED_DESCRIPTION"],
                bd_name=row['PROPOSED_BD'],
                vrf_name=row['PROPOSED_VRF'],)
            epg_lst.append(row["VLAN_ID"])
            logfile.write(epg)
            logfile.write("\n\n")
            logfile.write(bridge_domain)
            logfile.write("\n\n")
            print(epg)
    logfile.close()




main()
