#GetJMADataの定義、JSONとってくる
def GetJMAData(request):
    try:
        res = requests.get(request,verify=False)
        return res.json()
    except Exception:
        return None