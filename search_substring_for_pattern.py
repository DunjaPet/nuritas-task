import copy
from collections import Counter 

# real sequence
#txt="ITAGDKIWAIIAGDPEILDRAVQMISPDHDELRVAVPLGFNNLPAHSTIEVYVLEKITLTLMFRGLGVTKPLQTRGAAGRGLITDSYKTAEIIVSRAVGYTITKSGKHPPGSPQIACFMKNMRFQKARTHVLGSALNDGFFIDLAADIKALVEPQVAPCSTAKQASRLSAPEKSPTTQTPTGRGLIQAIRVPERVKLQLTIVVVVGGAPYPTCTSTAGGLAAFRALVIMSVPGLVVLSISKCTQGPKGIANDPSLTYKPAGAERGKIVHGSLWVSLRIKTGAANEKVWEVWGIMAAQPITSEKTIMQQIKRVPLAGLQSLVLVGTSIVDIGVSYYALLMGKLTVEENQTELVFAEAPSLQLIDFDVRHIYRATIDGVFMGGVDIKDGGMEELPDPKTKAGLSAKDNVARALMECTNDVSPYSDIQIPLRSDSLAAYADLKISLETIRAHYNIGVGVALARELSLYNFLAKAGLEKEVQNTMTEQFVHLYESRKNDLYKLVRDYGSLEIPEKGYLVVYMQDAAPLDGSRANMMIPGGGTINVSQRLVSIVAYCNSYALAPNSAAVGALGVANIQNLSLLNLHLIEGKIGEYKQLVLYTGQTLTQAKKMVERFYASQSDLVEAIFIGAQYSIVLFYPPLQGKPFRWPFISCEELASPPNHCHTRSRYLVGLAYYVSQNSPAHTDEFVFEPKDKYFVIALELCSMKSITALRKTDMMYLDVKHQLSNFEDSIGLVLPLSFTHFNAVMHLGKRVSRIATIRAHALEFGDIAFISSAQPFDWAGKSAKFSAPDKQLPYRELSANR"
# test sequence below
txt="HDELRVAVPLGFNNLPAHSTIEVYVLE"


hashTB = []
lens=[]


#--------------- functions----------------

def checkrow(txt,ptn):
	for j in range(len(txt)-len(ptn)+1):						# second dimension for hashTB
		hashTB.append([])	
		ptnC = copy.deepcopy(ptn)						# copy ptn in every itteration		
		for i in range(j,len(txt)):    						# itterating trough txt  (one dimension)
					
			if txt[i] in ptnC:   						# check i-th letter in txt if is in ptn 
							
				ptnC.remove(txt[i])
				hashTB[j].append(1)
				
				if len(ptnC)==0:
						break		
			else:
				hashTB[j].append(0)
			
		if sum(hashTB[j])==len(ptn):
			lens.append(len(hashTB[j]))

	return min(lens)




def excess_letters (txt):
	
		ptn=[]
		freqs = Counter(txt)
		if	len(txt)==800:
		
			for k,v in freqs.items():
				if v > 40:		
					value = v - 40
					ptn.append([k]*value)
							
				else:
					continue
					
			flat_ptn = [item for sublist in ptn for item in sublist]
				
			return flat_ptn
		else:
			print ("bad sequence")
			

ptn = excess_letters(txt)

print (checkrow(txt,ptn))
