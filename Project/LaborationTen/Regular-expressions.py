import re

def taskOneAndTwo():
    mtxt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."
    test = re.findall(r"(?:^|\s)([\w.]+?@[\w]+\.[\w\.]+[\w])", mtxt)
    #print(test)
    
def taskThree():
    f = open(r"C:\Users\gabri\OneDrive\Dokument\GitHub\NetworkProgramming\Project\LaborationTen\tabla.html","r" , encoding="utf-8")
    txt = f.read()
    tasklast = re.findall(r'<td class="svtTablaTime">\s+' 
                          r'(\d+\.\d+)\s+' 
                          r'</td>'
                          r'<td class=\"svtJsTablaShowInfo\">\s+'
                          r'<h4 class=\"svtLink-hover svtTablaHeading\">\s'
                          r'Simpsons\s+'
                          r'</h4>\s+'
                          r'<div class=\"svtJsStopPropagation\">\s+'
                          r'<div class=\"svtTablaTitleInfo svtHide-Js\">\s+'
                          r'<div class=\"svtTablaContent-Description\">\s+'
                          r'<p class=\"svtXMargin-Bottom-10px\">\s+Amerikansk animerad komediserie från [\d-]+\. Säsong (\d+)\. Del [\d+] av (\d+)\.(.+?)\s+' 
                          r'</p>',txt)

    for x in tasklast:
        time = x[0]
        season = x[1]
        episode = x[2] + "\\" + x[3]
        description = [4]
                            
        print(time, season, episode,description)               

taskOneAndTwo()
taskThree()