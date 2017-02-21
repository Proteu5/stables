###
from anytree import Node, RenderTree

talc = Node("Tale of the Cat", win=1, race=5)
satn = Node("Satin Sunrise", win=0, race=0)
lionH = Node("Lion Heart", parent=talc, win=5, race=10)
lionH = Node("Lion Heart", parent=satn, win=5, race=10)
kanth = Node("Kantharos", parent=lionH, win=3, race=3)
ansec = Node("Ancient Secret", parent=kanth, win=4, race=6)
satnS = Node("Satin Sunrise", win=0, race=0)
southH = Node("Southern Halo", win=0, race=2)
contH = Node("Contessa Halo", parent=southH, win=0, race=0)
kanth = Node("Kantharos", parent=contH, win=3, race=3)
queen = Node("Queen of Savoy", win=0, race=0)
contH = Node("Contessa Halo", parent=queen, win=0, race=0)

weldec = Node("Well Decorated", win=0, race=1)
nbk = Node("Notebook", parent=weldec, win=0, race=0)
prvcy = Node("Privacy", parent=nbk, win=1, race=4)
ansec = Node("Ancient Secret", parent=prvcy, win=4, race=6)
prvtAccnt = Node("Private Account", win=0, race=1)
prvtFun = Node("Private Fun", parent=prvtAccnt, win=0, race=0)
prvcy = Node("Privacy", parent=prvtFun, win=1, race=4)
mobcap = Node("Mobcap")
funist = Node("Funistrada", win=0, race=1)
nbk = Node("Notebook", parent=mobcap, win=0, race=0)
prvtFun = Node("Private Fun", parent=funist, win=0, race=0)
prvcy = Node("Privacy", parent=prvtFun, win=1, race=4)
#joe = Node("Joe", parent=dan)

#print(talc)
#Node('Udo')
#print(southH)
#Node('Udo/Dan/Joe')

for pre, fill, node in RenderTree(talc):
    print("%s%s" % (pre, node.name))
for pre, fill, node in RenderTree(satn):
    print("%s%s" % (pre, node.name))
for pre, fill, node in RenderTree(southH):
    print("%s%s" % (pre, node.name))
for pre, fill, node in RenderTree(queen):
    print("%s%s" % (pre, node.name))

for pre, fill, node in RenderTree(weldec):
    print("%s%s" % (pre, node.name))
for pre, fill, node in RenderTree(mobcap):
    print("%s%s" % (pre, node.name))
for pre, fill, node in RenderTree(prvtAccnt):
    print("%s%s" % (pre, node.name))
for pre, fill, node in RenderTree(funist):
    print("%s%s" % (pre, node.name))

#print(dan.children)
#(Node('Udo/Dan/Jet'), Node('Udo/Dan/Jan'), Node('Udo/Dan/Joe'))
print("\n\n")
print(RenderTree(talc))
print(RenderTree(satn))
print(RenderTree(southH))
print(RenderTree(queen))
print(RenderTree(weldec))
print(RenderTree(mobcap))
print(RenderTree(prvtAccnt))
print(RenderTree(funist))

talc_win_ratio = float(talc.win) / talc.race
lionH_win_ratio = float(lionH.win) / lionH.race
kanth_win_ratio = float(kanth.win) / kanth.race
ansec_win_ratio = float(ansec.win) / ansec.race
weldec_win_ratio = float(weldec.win) / weldec.race
prvcy_win_ratio = float(prvcy.win) / prvcy.race
prvtAccnt_win_ratio = float(prvtAccnt.win) / prvtAccnt.race
funist_win_ratio = float(funist.win) / funist.race
#satn_win_ratio = float(satn.win) / satn.race
print("\n-----\n" +str(talc)+ "\nRatio: " +str(talc_win_ratio))
print("\n-----\n" +str(lionH)+ "\nRatio: " +str(lionH_win_ratio))
print("\n-----\n" +str(kanth)+ "\nRatio: " +str(kanth_win_ratio))
print("\n-----\n" +str(ansec)+ "\nRatio: " +str(ansec_win_ratio))
print("\n-----\n" +str(weldec)+ "\nRatio: " +str(weldec_win_ratio))
print("\n-----\n" +str(prvcy)+ "\nRatio: " +str(prvcy_win_ratio))
print("\n-----\n" +str(prvtAccnt)+ "\nRatio: " +str(prvtAccnt_win_ratio))
print("\n-----\n" +str(funist)+ "\nRatio: " +str(funist_win_ratio))

tlk_win_avg_sum = talc_win_ratio + lionH_win_ratio + kanth_win_ratio
tlk_win_avg = float(tlk_win_avg_sum) / 3
print("\n----\nAverage Ratios:\n" +str(talc)+ "\n" +str(lionH)+ "\n" +str(kanth)+ "\nRatio: "+str(tlk_win_avg))
print("\n" +str(ansec)+ "\nAncient Secret Ratio: " +str(ansec_win_ratio))

tl_win_avg_sum = talc_win_ratio + lionH_win_ratio
tl_win_avg = float(tl_win_avg_sum) / 2
print("\n----\nAverage Ratios:\n" +str(talc)+ "\n" +str(lionH)+ "\n" +str(tl_win_avg))
print("\n" +str(kanth)+ "\nKantharos Ratio: " +str(kanth_win_ratio))

tlka_win_avg_sum = talc_win_ratio + lionH_win_ratio + kanth_win_ratio + ansec_win_ratio
tlka_win_avg = float(tlka_win_avg_sum) / 4
print("\n----\nAverage Ratios:\n" +str(talc)+ "\n" +str(lionH)+ "\n" +str(kanth)+ "\n" +str(ansec)+  "\nRatio: "+str(tlka_win_avg))

delta_tlka = tlka_win_avg - tlk_win_avg
delta_tlk = tlk_win_avg - tl_win_avg
print("Generational Delta A: "+str(delta_tlka)+ "\nGenerational Delta B: " +str(delta_tlk))

tlka_plus_delta = tlka_win_avg + delta_tlka
print("GenA + TLKA Ratio: " +str(tlka_plus_delta))

tlk_plus_delta = tlk_win_avg + delta_tlk
print("GenB + TLK Ratio: " +str(tlk_plus_delta))
ansecProfrmanceRatio = tlk_plus_delta - ansec_win_ratio
print("Ancient Secret Preformance Ratio: " +str(ansecProfrmanceRatio))