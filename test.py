import ast
# s = ast.literal_eval(0x90)
# print(s)
# ver = 96
# verz = '0x'+str(ver)
# print(verz)
b = 'VB96.BIN'
bmsversion = b.split('.')[0]
print(bmsversion)
BMS_Version = bmsversion.replace('V','')
print(BMS_Version)
temp = BMS_Version.replace('B','')
BMS_VersionNo_HEX = '0x'+str(temp)
print(BMS_VersionNo_HEX)
BMS_VersionNo_INT = ast.literal_eval(BMS_VersionNo_HEX)
print(BMS_VersionNo_INT)
BMS_versions_available.append(int(BMS_VersionNo))
