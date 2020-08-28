from hinterlist import check

c = check.Checker()
result = c.run_check(xtf=r"\\v0t0020a.adr.admin.ch\iprod\gdwh-etl\PURE\acquisition\dm01\all\0012.itf",
                     ili=r"\\v0t0020a.adr.admin.ch\iprod\gdwh-etl\PURE\schema\ili\DM01AVCH24LV95D.ili",
                     mode=check.Mode.SYNC,
                     config=check.Config.INTERLIS)

print(result.jobid)
print(result.logfile)
print(result.success)
print(result.valid)
