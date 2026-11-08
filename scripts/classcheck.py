import re,sys
def css_classes(s):
    css="".join(re.findall(r"<style[^>]*>(.*?)</style>",s,re.S))
    return css
def check(f):
    s=open(f,encoding="utf-8").read(); css=css_classes(s)
    body=s[s.index("<body"):]
    used=set(c for m in re.findall(r'class="([^"]*)"',body) for c in m.split())
    missing=[]
    for c in used:
        e=re.sub(r'([:\[\]\./%#()])',r'\\\1',c)
        if "."+e not in css: missing.append(c)
    return missing
for f in sys.argv[1:]:
    m=check(f)
    if m: print(f, sorted(m))
print("checked",len(sys.argv)-1)
