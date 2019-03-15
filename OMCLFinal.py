# Script that reads three files and outputs an annotated list of transcripts (with orthoMCL clusters) and a list of clusters
# please change input and output files according to your requirements!
# M. Cordellier 19.03.2018
# usage python ClusteringAll.py <1 OrthoMCLFile> <2 blue network genes> <3 brown network genes> <4 JA genes> 
# <5 output blue tr> <6 output brown tr> <7 output JA tr> 
# <8 output blue clusterList> <9 output brown clusterList> <10 output JA clusterList> 
# <11 intersection blue JA> <12 intersection brown JA> <13 intersection repro> <14 subset orthoMCL> 


#python OMCLFinal.py
orthomcl_daphnia_orthology_okayset.txt blue-gene.txt brown-gene.txt Genelist.General_JA.txt BlueAnnotated.txt BrownAnnotated.txt JA_Annotated.txt BlueClusterlist.txt BrownClusterlist.txt JAClusterlist.txt IntersectBlueJA.txt IntersectBrownJA.txt reproDpulDgal.txt subsetOMCL.txt




import sys
import re

OMCL = open(sys.argv[1], "r")

###########def blueclusters():

bluenetwork = open(sys.argv[2], "r")
outfile5 = open(sys.argv[5], "w")
outfile8 = open(sys.argv[8], "w")
blueclusterList=set()

for line in bluenetwork:
	clu = ''
	line = line.rstrip('\n')
	cand = line.split(",")[0]
	Tr = (cand + ' ')

	for line in OMCL:
		clusterLine = line.rstrip('\n')
		cluster = clusterLine.split(":")[0]
		
		if Tr in clusterLine:
			clu = cluster
			blueclusterList.add(clu)

	OMCL.seek(0)
	
	outfile5.write(cand+"\t"+clu+"\n")

outfile8.write("\n".join(blueclusterList)+"\n")

outfile5.close()
bluenetwork.close()
outfile8.close()
print "finished with blue!"


#############def brownclusters():

brownnetwork = open(sys.argv[3], "r")
outfile6 = open(sys.argv[6], "w")
outfile9 = open(sys.argv[9], "w")
brownclusterList=set()

for line in brownnetwork:
	clu = ''
	line = line.rstrip('\n')
	cand = line.split(",")[0]
	Tr = (cand + ' ')

	for line in OMCL:
		clusterLine = line.rstrip('\n')
		cluster = clusterLine.split(":")[0]
		
		if Tr in clusterLine:
			clu = cluster
			brownclusterList.add(clu)

	OMCL.seek(0)
	
	outfile6.write(cand+"\t"+clu+"\n")

outfile9.write("\n".join(brownclusterList)+"\n")

outfile6.close()
outfile9.close()
brownnetwork.close()
print "finished with brown!"



##############def JAclusters():

JACand = open(sys.argv[4], "r")
outfile7 = open(sys.argv[7], "w")
outfile10 = open(sys.argv[10], "w")
JAclusterList=set()

for line in JACand:
	clu = ''
	line = line.rstrip('\n')
	cand = line.split('\t')[0]
	Tr = (cand + ' ')
		
	for line in OMCL:
		
		clusterLine = line.rstrip('\n')
		cluster = clusterLine.split(":")[0]
		
		if Tr in clusterLine:
			clu = cluster
			JAclusterList.add(clu)
	OMCL.seek(0)
	
	outfile7.write(cand+"\t"+clu+"\n")

outfile10.write("\n".join(JAclusterList)+"\n")

JACand.close()
outfile7.close()
outfile10.close()
print "finished with Jana's candidates!"





#################def compareClusterLists():
outfile11 = open(sys.argv[11], "w")
outfile12 = open(sys.argv[12], "w")
outfile13 = open(sys.argv[13], "w")

blueIntersect=set()
brownIntersect=set()
reproDpulDgal=set()

blueIntersect = blueclusterList.intersection(JAclusterList)
brownIntersect = brownclusterList.intersection(JAclusterList)
reproDpulDgal = blueIntersect.union(brownIntersect)

#output lists!
outfile11.write("\n".join(blueIntersect)+"\n")
outfile12.write("\n".join(brownIntersect)+"\n")
outfile13.write("\n".join(reproDpulDgal)+"\n")

outfile11.close()
outfile12.close()
outfile13.close()

print "done with Intersections"

#### subset OrthoMCL
outfile14 = open(sys.argv[14], "w")

for line in OMCL:
	
	clusterLine = line.rstrip('\n')
	cluster = clusterLine.split(":")[0]
		
	if cluster in reproDpulDgal:
		outfile14.write(clusterLine+"\n")	
OMCL.seek(0)

outfile14.close()
OMCL.close()
	
