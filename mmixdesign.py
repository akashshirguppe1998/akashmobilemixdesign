import streamlit as st

from streamlit_option_menu import option_menu
from PIL import Image

hide_st_style="""
	<style>
	#MainMenu{visibility:hidden;}
	footer{visibility:hidden;}
	</style>
	"""
st.markdown(hide_st_style,unsafe_allow_html=True)









st.image(Image.open('AK11.png'))
selected=option_menu(
	menu_title =None,
	options =["INSTRUCTIONS","MIX DESIGN","ABOUT ME"],
	orientation="horizontal",




	)


if selected=="INSTRUCTIONS":
	st.title(f"{selected}")
	st.write("****")
	st.write("1) The mix design calculations are done using **IS 10262-2019**.")
	st.write("2) Concrete of strength of M20 to M80 can be done effectively using this web app.")
	st.write("3) Enter the input values correctly to get accurate results.")
	st.write("4) The water cement ratio is determined using the Fig.1  and Table 8 of IS 10262-2019.")
	st.write("5) The approximate air content is taken from the Table 3 and Table 6 of IS 10262-2019.")
	st.write("5) The dosages of mineral admixture should be taken from the Table 9 of IS 10262-2019.")
	st.write("5) Addtion of upto 3 mineral admixture as cementitious material has been allowed in this app.But care should be taken by user about codal provisions minimum Cement(OPC) content")
	st.write("6) Use expander **DETAILED OUTPUT** for detailed output as in ANNEXURES of IS 10262-2019")
	st.write("7) Trail 1 results are for aggregates in SSD condition, Trail 2 results are for adjustments done for wet (OR) dry condition aggregates.")


if selected=="ABOUT ME":
	col1,col2,col3=st.columns(3)
	with col2:
		st.title(f"{selected}")
	st.write("****")
	col1,col2,col3=st.columns(3)
	with col1:
		st.image(Image.open('ak11.jpg'))
	with col2:	
		st.header("***AKASH SHIRGUPPE***")

	with col3:	
		st.write("*Qualification:*")
		st.write("***BE (Civil Engineering-2021)***")
		st.write("***Mtech Structural Engineering (Pursuing)***")
		st.write("*Contact details*")	
		st.write("***Email: akashshirguppe@gmail.com***")


if selected=="MIX DESIGN":
	st.title("CONCRETE MIX DESIGN")
	st.write("***(AS PER IS 10262-2019)***")
	st.write("****")

	col1, col2= st.columns(2)
	with col1:
		st.write("**TARGET STRENGTH OF CONCRETE**")
		fck=st.number_input("ENTER THE GRADE OF CONCRETE",min_value=20,max_value=100,step=5)
	with col2:
		st.write("**FRESH CONCRETE PROPERTIES**")
		Slump=st.number_input("SLUMP IN MM ")
		MOP=st.checkbox("PUMPABLE")


	st.write("**CEMENT**")
	col1, col2= st.columns(2)
	with col1:
		OPC=st.number_input("GRADE OF CEMENT")
	with col2:
		SpCement=st.number_input("SPECIFIC GRAVITY OF CEMENT")	

	col1,col2=st.columns(2)
	with col1:
		st.write("**COARSE AGGREGATE**")
		SpCA=st.number_input("SPECIFIC GRAVITY COARSE AGGREGATE")
	with col2:
		st.write("**FINE AGGREGATE**")	
		SpFA=st.number_input("SPECIFIC GRAVITY FINE AGGREGATE")

	col1, col2, col3=st.columns([1,3,4])
	with col1:
		if fck<65:
			CAgg=["10","20","40"]
			cagg=st.radio("*SIZE(MM)*",CAgg)
		elif fck>=65:
			CAgg=["10","12.5","20"]
			cagg=st.radio("*SIZE(MM)*",CAgg)
	with col2:	
		CAsh=["ANGULAR","SUB-ANGULAR","GRAVEL(CRUSHED PARTICLES)","ROUNDED GRAVEL"]
		cash=st.radio("*SHAPE OF AGGREGATES*",CAsh)
	with col3:
		if fck<65:
			Zones=["I","II","III","IV"]
			
			zone=st.radio("*ZONES OF FINE AGGREGATES*",Zones)
		elif fck>=65:
			Zones=["I","II","III"]
			#st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
			zone=st.radio("*ZONES OF FINE AGGREGATES*",Zones)




	st.write("**CHEMICAL ADMIXTURE (PLASTICISER)**")
	col1,col2,col3=st.columns(3)
	with col1:
		Plasti=st.number_input("WATER CONTENT REDUCTION IN % ")
	with col2:
		PerPlasti=st.number_input("DOSAGE OF PLASTICISER IN % ")
	with col3:	
		SpPlastic=st.number_input("SPECIFIC GRAVITY PLASTICISER")

	st.write("**MINERAL ADMIXTURE**")
	PerInCem=st.number_input("PERCENTAGE INCREASE IN CEMENTITIOUS MATERIAL")
	col1, col2= st.columns(2)
	with col1:
		l=st.number_input("ADMIXTURE 1 REPLACEMENT PERCENTAGE")
	with col2:
		l1=st.number_input("SPECIFIC GRAVITY MINERAL ADMIXTURE 1")
	col1, col2= st.columns(2)
	with col1:
		m=st.number_input("ADMIXTURE 2 REPLACEMENT PERCENTAGE")
	with col2:
		m1=st.number_input("SPECIFIC GRAVITY MINERAL ADMIXTURE 2")
	col1, col2= st.columns(2)
	with col1:
		n=st.number_input("ADMIXTURE 3 REPLACEMENT PERCENTAGE")
	with col2:
		n1=st.number_input("SPECIFIC GRAVITY MINERAL ADMIXTURE 3")

	st.write("**MOISTURE CONTENT**")
	col1,col2=st.columns(2)
	with col1:
		MoCo1=st.number_input("MOISTURE CONTENT COARSE AGGREGATE")
	with col2:
		MoCo2=st.number_input("MOISTURE CONTENT FINE AGGREGATE")

	st.write("**WATER ABSORPTION**")
	col1,col2=st.columns(2)
	with col1:
		Wab1=st.number_input("WATER ABSORPTION COARSE AGGREGATE")
	with col2:
		Wab2=st.number_input("WATER ABSORPTION FINE AGGREGATE")





	                 ###########CALCULATION OF MIX DESIGN#########
	if fck==10:
		fc10a=fck+int(5)
		fc10b=fck+float(1.65*3.5)
		fcf=max(fc10a,fc10b)
	elif fck==15:
		fc15a=fck+int(5)
		fc15b=fck+float(1.65*3.5)
		fcf=max(fc15a,fc15b)
	elif fck==20:
		fc20a=fck+float(5.5)
		fc20b=fck+float(1.65*4)
		fcf=max(fc20a,fc20b)
	elif fck==25:
		fc25a=fck+float(5.5)
		fc25b=fck+float(1.65*4)
		fcf=max(fc25a,fc25b)
	elif fck==30:
		fc30a=fck+float(6.5)
		fc30b=fck+float(1.65*5)
		fcf=max(fc30a,fc30b)
	elif fck==35:
		fc35a=fck+float(6.5)
		fc35b=fck+float(1.65*5)
		fcf=max(fc35a,fc35b)
	elif fck==40:
		fc40a=fck+float(6.5)
		fc40b=fck+float(1.65*5)
		fcf=max(fc40a,fc40b)
	elif fck==45:
		fc45a=fck+float(6.5)
		fc45b=fck+float(1.65*5)
		fcf=max(fc45a,fc45b)
	elif fck==50:
		fc50a=fck+float(6.5)
		fc50b=fck+float(1.65*5)
		fcf=max(fc50a,fc50b)
	elif fck==55:
		fc55a=fck+float(6.5)
		fc55b=fck+float(1.65*5)
		fcf=max(fc55a,fc55b)
	elif fck==60:
		fc60a=fck+float(6.5)
		fc60b=fck+float(1.65*5)
		fcf=max(fc60a,fc60b)
	elif fck==65:
		fc65a=fck+float(8)
		fc65b=fck+float(1.65*6)
		fcf=max(fc65a,fc65b)
	elif fck==70:
		fc70a=fck+float(8)
		fc70b=fck+float(1.65*6)
		fcf=max(fc70a,fc70b)
	elif fck==75:
		fc75a=fck+float(8)
		fc75b=fck+float(1.65*6)
		fcf=max(fc75a,fc75b)

	elif fck>=80:
		fc80a=fck+float(8)
		fc80b=fck+float(1.65*6)
		fcf=max(fc80a,fc80b)
		j=int(10)*(fcf//int(10))
		k=j+10


	#Calculation of water cement ratio		
	j=int(10)*(fcf//int(10))
	k=j+10
	if OPC<=42:
		if j==20 and k==30:
			w_c=float(0.5625)-((float(0.5625)-float(0.45))*(fcf-int(20))/(int(30)-int(20)))
		elif j==30 and k==40:
			w_c=float(0.45)-((float(0.45)-float(0.36875))*(fcf-int(30))/(int(40)-int(30)))
		elif j==40 and k==50:
			w_c=float(0.36875)-((float(0.36875)-float(0.3))*(fcf-int(40))/(int(50)-int(40)))
		elif j==50 and k==60:
			w_c=float(0.3)-((float(0.3)-float(0.25))*(fcf-int(50))/(int(60)-int(50)))
	if OPC<=52:
		if j==20 and k==30:
			w_c=float(0.625)-((float(0.625)-float(0.5))*(fcf-int(20))/(int(30)-int(20)))
		elif j==30 and k==40:
			w_c=float(0.5)-((float(0.5)-float(0.4125))*(fcf-int(30))/(int(40)-int(30)))
		elif j==40 and k==50:
			w_c=float(0.4125)-((float(0.4125)-float(0.3375))*(fcf-int(40))/(int(50)-int(40)))
		elif j==50 and k==60:
			w_c=float(0.3375)-((float(0.3375)-float(0.28125))*(fcf-int(50))/(int(60)-int(50)))
		elif j==60 and k==70:
			w_c=float(0.28125)-((float(0.28125)-float(0.25))*(fcf-int(70))/(int(80)-int(70)))	
	if OPC>=53:
		if j==30 and k==40:
			w_c=float(0.575)-((float(0.57)-float(0.475))*(fcf-int(30))/(int(40)-int(30)))
		elif j==40 and k==50:
			w_c=float(0.475)-((float(0.475)-float(0.39375))*(fcf-int(40))/(int(50)-int(40)))
		elif j==50 and k==60:
			w_c=float(0.39375)-((float(0.39375)-float(0.33125))*(fcf-int(50))/(int(60)-int(50)))
		elif j==60 and k==70:
			w_c=float(0.33125)-((float(0.33125)-float(0.275))*(fcf-int(60))/(int(70)-int(60)))	
		elif j==70 and k==80:
			if cagg=='10':
				w_c=float(0.36)-((float(0.36)-float(0.32))*(fcf-int(70))/(int(80)-int(70)))
			elif cagg=='12.5':
				w_c=float(0.35)-((float(0.35)-float(0.31))*(fcf-int(70))/(int(80)-int(70)))
			elif cagg=='20':
				w_c=float(0.33)-((float(0.33)-float(0.29))*(fcf-int(70))/(int(80)-int(70)))	
		elif j==80 and k==90:
			if cagg=='10':
				w_c=float(0.32)-((float(0.32)-float(0.28))*(fcf-int(80))/(int(90)-int(80)))
			elif cagg=='12.5':
				w_c=float(0.31)-((float(0.31)-float(0.27))*(fcf-int(80))/(int(90)-int(80)))
			elif cagg=='20':
				w_c=float(0.29)-((float(0.29)-float(0.26))*(fcf-int(80))/(int(90)-int(80)))			



	#Entrapped air content and water content calculation
	if fck<65: 
		if cagg=='10':
			b=0.015
			z=(Slump-float(50))/float(25)
			water=208+(z*0.03*208)
			water1=water*(int(1)-Plasti*float(0.01))
			
		elif cagg=='20':
			b=0.01
			z=(Slump-float(50))/float(25)
			water=186+(z*0.03*186)
			water1=water*(int(1)-Plasti*float(0.01))

		elif cagg=='40':
			b=0.008
			z=(Slump-float(50))/float(25)
			water=165+(z*0.03*165)
			water1=water*(int(1)-Plasti*float(0.01))
		#st.write(water1)

		if cash=='ANGULAR':
			water2=water1
		elif cash=='SUB-ANGULAR':
			water2=water1-float(10)
		elif cash=='GRAVEL(CRUSHED)':
			water2=water1-float(15)
		elif cash=='ROUNDED GRAVEL':
			water2=water1-float(20)
		

	if fck>=65:
		if cagg=='10':
			b=0.01
			z=(Slump-float(50))/float(25)
			water=200+(z*0.03*200)
			water2=water*(int(1)-Plasti*float(0.01))
		elif cagg=='12.5':
			b=0.008
			z=(Slump-float(50))/float(25)
			water=195+(z*0.03*195)
			water2=water*(int(1)-Plasti*float(0.01))
		elif cagg=='20':
			b=0.005
			z=(Slump-float(50))/float(25)
			water=186+(z*0.03*186)
			water2=water*(int(1)-Plasti*float(0.01))

	#Calculation of cement content
	if l==0 and m==0 and n==0:
		w_cmp=w_c
		Cement1=round(water2/w_cmp)
		Q1=Cement1
	else:
		Cement=round(water2/w_c)
		Q=round(Cement*(float(1)+(PerInCem*float(0.01))))
		if m==0 and n==0:
			l2=round(Q*l*float(0.01))
			Vl3=(l2)/(l1*int(1000))
			Cement1=Q-l2
			
		
		elif n==0:
			l2=round(Q*l*float(0.01))
			Vl3=(l2)/(l1*int(1000))
			m2=round(Q*m*float(0.01))
			Vm3=(m2)/(m1*int(1000))
			Cement1=Q-l2-m2
			
		else:
			l2=round(Q*l*float(0.01))
			Vl3=(l2)/(l1*int(1000))	
			m2=round(Q*m*float(0.01))
			Vm3=(m2)/(m1*int(1000))
			n2=round(Q*n*float(0.01))
			Vn3=(n2)/(n1*int(1000))
			Cement1=Q-l2-m2-n2
			
		w_cmp=water2/Q
		Q1=Q




		##Volume of coarse aggregate	
	if fck<65:
		if cagg=='10':
			if zone=='I':
				Vocg=0.48
			elif zone=='II':
				Vocg=0.50
			elif zone=='III':
				Vocg=0.52
			elif zone=='IV':
				Vocg=0.54
		if cagg=='20':
			if zone=='I':
				Vocg=0.60
			elif zone=='II':
				Vocg=0.62
			elif zone=='III':
				Vocg=0.64
			elif zone=='IV':
				Vocg=0.66
		if cagg=='40':
			if zone=='I':
				Vocg=0.69
			elif zone=='II':
				Vocg=0.71
			elif zone=='III':
				Vocg=0.72
			elif zone=='IV':
				Vocg=0.73
		VolCA=Vocg+((float(0.5)-w_cmp)/float(5))
		if MOP:
			#st.write("CONCRETE IS Pumpable")
			VolCA1=float(0.9)*VolCA					
		else:
			VolCA1=VolCA
		#st.write("PERCENT OF cg **%.3f** m^3 for w/c of 0.5" %Vocg)
		#st.write("CORRECTED PERCENT OF cg **%.3f** m^3 for w/c of 0.5" %VolCA1)	

	if fck>=65:
		if cagg=='10':
			if zone=='I':
				Vocg=0.52
			elif zone=='II':
				Vocg=0.54
			elif zone=='III':
				Vocg=0.56
		if cagg=='20':
			if zone=='I':
				Vocg=0.64
			elif zone=='II':
				Vocg=0.66
			elif zone=='III':
				Vocg=0.68	
		if cagg=='12.5':
			if zone=='I':
				Vocg=0.54
			elif zone=='II':
				Vocg=0.56
			elif zone=='III':
				Vocg=0.58
		VolCA=Vocg+((float(0.3)-w_cmp)/float(5))
		if MOP:		
			#st.write("CONCRETE IS Pumpable")
			VolCA1=float(0.95)*VolCA	
		else:
			VolCA1=VolCA			
		#st.write("PERCENT OF cg **%.3f** m^3 for w/c of 0.3" %Vocg)
		#st.write("CORRECTED PERCENT OF cg **%.3f** m^3 for w/c of 0.3" %VolCA1)		
	 

	VolFA=float(1)-VolCA1
	#st.write("PERCENT OF fg **%.3f** m^3 " %VolFA)






	#MIX DESIGN CALCULATIONS

	#VOLUME OF ENTRAPPED AIR=b
	#VOLUME OF CEMENT
	C=(Cement1)/(SpCement*int(1000))
	#VOLUME OF WATER
	W=(water2/int(1000))
	#Volume of plasticiser
	if PerPlasti!=0:
		P1=round((float(0.01)*PerPlasti*Q1),4)
		P=(float(0.01)*PerPlasti*Q1)/(SpPlastic*int(1000))
	else:
		P=0
		P1=0
	#VOLUME OF ALL IN ONE AGGREGATES
	if l==0 and m==0 and n==0:
		G=float(1)-b-C-W-P
	else:
		if m==0 and n==0:
			G=float(1)-b-C-W-P-Vl3
		elif n==0:
			G=float(1)-b-C-W-P-Vl3-Vm3
		else:
			G=float(1)-b-C-W-P-Vl3-Vm3-Vn3



	#st.write(b)
	#st.write(C)
	#st.write(W)
	#st.write(P)
	#st.write(G)
	#MASS OF COARSE AGGREGATE
	MCA=round(G*SpCA*VolCA1*int(1000))
	#MASS OF FINE AGGREGATE
	MFA=round(G*SpFA*VolFA*int(1000))
	#st.write("MASS OF COARSE AGGREGATE IS %d Kg  " %MCA)
	#st.write("MASS OF FINE AGGREGATE IS %d Kg" %MFA)

	#ADUSTMENT FOR WATER ABSORPTION#
	FrMoCo1=MoCo1-Wab1
	FrMoCo2=MoCo2-Wab2
	if FrMoCo1<=0:
		MCA1=round(MCA/(int(1)+(float(0.01)*(-FrMoCo1))))
		z1=MCA-MCA1
	elif FrMoCo1>0:
		MCA1=round(MCA*(int(1)+(float(0.01)*FrMoCo1)))
		z1=MCA-MCA1

	if FrMoCo2<=0:
		MFA1=round(MFA/(int(1)+(float(0.01)*(-FrMoCo2))))
		z2=MFA-MFA1
	elif FrMoCo2>0:
		MFA1=round(MFA*(int(1)+(float(0.01)*FrMoCo2)))
		z2=MFA-MFA1

	water22=round(water2+z1+z2)
	#st.write(z1)
	#st.write(z2)
	#st.write(MCA1)
	#st.write(MFA1)
	#st.write(water22)



	## METRIC DISPLAY OF RESULTS ##
	st.write("******")
	if st.button("GET MIX PROPORTION"):
		st.write("**TRAIL 1 (By weight)**")
		st.write("(*All in Kg/m^3*)")	
		col1,col2,col3,col4=st.columns(4)
		col1.metric(label="**CEMENT**",value=Cement1)
		col2.metric(label="**WATER**",value=round(water2))
		col3.metric(label="**COARSE AGGREGATE(SSD)**",value=MCA)
		col4.metric(label="**FINE AGGREGATE(SSD)**",value=MFA)

		if l==0 and m==0 and n==0:
			col1.metric(label="**CHEM.ADMIXTURE**",value=P1)
		else:
			if m==0 and n==0:
				col1,col2=st.columns(2)		
				col1.metric(label="**MIN.ADMIXTURE 1**",value=l2)
				col2.metric(label="**CHEM.ADMIXTURE**",value=P1)
			elif n==0:
				col1,col2,col3=st.columns(3)
				col1.metric(label="**MINERAL ADMIXTURE 1**",value=l2)
				col2.metric(label="**MINERAL ADMIXTURE 2**",value=m2)
				col3.metric(label="**CHEM.ADMIXTURE**",value=P1)
			else:
				col1,col2,col3,col4=st.columns(4)
				col1.metric(label="**MINERAL ADMIXTURE 1**",value=l2)
				col2.metric(label="**MINERAL ADMIXTURE 2**",value=m2)
				col3.metric(label="**MINERAL ADMIXTURE 3**",value=n2)
				col4.metric(label="**CHEM.ADMIXTURE**",value=P1)
		col1.metric(label="**WATER-CEMENT RATIO**",value=round(w_cmp,4))	
		st.write("******")

	## METRIC DISPLAY OF RESULTS TRAIL2 ##
		
	#EXPANDERS TO READ INPUT AND OUTPUT DETAILS
	with st.expander("**CLICK HERE FOR DETAILED OUTPUT**"):
		st.write("***")
		st.write("**1] TARGET STRENGTH FOR MIX PROPORTIONING**")
		st.write("Target strength of concrete = **%.2f N/mm^2** ." % fcf)
		st.write("***")
	


		st.write("**2] APPROXIMATE AIR CONTENT**")
		st.write("Approximate amount of entrapped air in normal concrete = **%.3f m^3**" % b)
		st.write("****")

		st.write("**3] SELECTION OF WATER CEMENT RATIO**")
		st.write("Water cement ratio = **%.4f**" % w_c)
		st.write("****")

		st.write("**4] SELECTION OF WATER CONTENT**")
		st.write("Water content = **%.3f Kg**" % water)
		st.write("Reduced water content due to plasticiser = **%.4f Kg**" %water2)
		st.write("****")

		st.write("**5] CALCULATION OF CEMENT CONTENT**")
		if l==0 and m==0 and n==0:
			st.write(" 5.1) CEMENT CONTENT = **%.3f Kg/m^3**" % Cement1)
			st.write("NO MINERAL ADMIXTURE ADDED")	
		else:
			if m==0 and n==0:
				st.write("5.1) CEMENT CONTENT = **%.3f Kg/m^3**" % Cement)
				st.write("5.2) CEMENTITIOUS MATERIAL CONTENT = **%.3f Kg/m^3**" % Q)
				st.write("5.3) WATER CEMENTITIOUS RATIO = **%.4f**" % w_cmp)
				st.write("5.4) 1st MINERAL ADMIXTURE CONTENT = **%.3f Kg/m^3**" % l2)
				st.write("5.5) CEMENT (OPC) CONTENT = **%.3f Kg/m^3**" % Cement1)
			elif n==0:
				st.write("5.1) CEMENT CONTENT = **%.3f Kg/m^2**" % Cement)
				st.write("5.2) CEMENTITIOUS MATERIAL CONTENT = **%.3f Kg/m^3**" % Q)
				st.write("5.3) WATER CEMENTITIOUS RATIO = **%.4f**" % w_cmp)
				st.write("5.4) 1st MINERAL ADMIXTURE CONTENT = **%.3f Kg/m^3**" % l2)
				st.write("5.5) 2nd MINERAL ADMIXTURE CONTENT = **%.3f Kg/m^3**" % m2)
				st.write("5.6) CEMENT (OPC) CONTENT = **%.3f Kg/m^3**" % Cement1)
			else:
				st.write("5.1) CEMENT CONTENT = **%.3f Kg/m^2**" % Cement)
				st.write("5.2) CEMENTITIOUS MATERIAL CONTENT = **%.3f Kg/m^3**" % Q)
				st.write("5.3) WATER CEMENTITIOUS RATIO = **%.4f**" % w_cmp)
				st.write("5.4) 1st MINERAL ADMIXTURE CONTENT = **%.3f Kg/m^3**" % l2)
				st.write("5.5) 2nd MINERAL ADMIXTURE CONTENT = **%.3f Kg/m^3**" % m2)
				st.write("5.6) 3rd MINERAL ADMIXTURE CONTENT = **%.3f Kg/m^3**" % n2)
				st.write("5.7) CEMENT (OPC) CONTENT = **%.3f Kg/m^3**" % Cement1)
		st.write("****")		

		st.write("**6] PROPORTIONING OF COARSE AGGREGATE AND FINE AGGREGATE CONTENT**")
		if fck<65:
			if MOP:	
				st.write("Volume of coarse aggregate = **%.3f** m^3 for w/c O.5 "%Vocg)
				st.write("For water cement ratio = **%.3f**"% w_cmp)
				st.write("Corrected proportion of volume of coarse aggregate =**%.3f** m^3 for w/c" %VolCA)
				st.write("***Concrete is Pumpable***")
				st.write("For pumping coarse aggregate volume = **%.3f** m^3 for w/c" %VolCA1)
			else:
				st.write("Volume of coarse aggregate = **%.3f** m^3 for w/c O.5 "%Vocg)
				st.write("For water cement ratio **%.3f**"% w_cmp)
				st.write("Corrected proportion of volume of coarse aggregate **%.3f** m^3 for w/c" %VolCA1)
		if fck>=65:
			if MOP:
				st.write("Volume of coarse aggregate = **%.3f** m^3 for w/c O.3 "%Vocg)
				st.write("For water cement ratio = **%.3f**"% w_cmp)
				st.write("Corrected proportion of volume of coarse aggregate =**%.3f** m^3 for w/c" %VolCA)
				st.write("***Concrete is Pumpable***")
				st.write("For pumping coarse aggregate volume = **%.3f** m^3 for w/c" %VolCA1)
			else:
				st.write("Volume of coarse aggregate = **%.3f** m^3 for w/c O.3 "%Vocg)
				st.write("For water cement ratio **%.3f**"% w_cmp)
				st.write("Corrected proportion of volume of coarse aggregate **%.3f** m^3 for w/c" %VolCA1)
					
		st.write("Volume of fine aggregate = **%.3f m^3** " %VolFA)
		st.write("****")	

		st.write("**7] MIX CALCULATIONS**")
		st.write("7.1) Total volume of concrete = **1 m^3**")
		st.write("7.2) Approximate volume of entrapped air in normal concrete = **%.3f m^3**" % b)
		if l==0 and m==0 and n==0:
			st.write("7.3.a) Volume of cement = **%0.4f m^3**" %C)
			st.write("7.3.b) Volume of water = **%0.4f m^3**" %W)
		else:
			if m==0 and n==0:
				st.write("7.3.a) Volume of cement = **%0.4f m^3**" %C)
				st.write("7.3.b) Volume of water = **%0.4f m^3**" %W)
				st.write("7.3.b) Volume of 1st mineral admixture = **%0.4f m^3**" %Vl3)
			elif n==0:
				st.write("7.3.a) Volume of cement = **%0.4f m^3**" %C)
				st.write("7.3.b) Volume of water = **%0.4f m^3**" %W)
				st.write("7.3.c) Volume of 1st mineral admixture = **%0.4f m^3**" %Vl3)
				st.write("7.3.d) Volume of 2nd mineral admixture = **%0.4f m^3**" %Vm3)	
			else:
				st.write("7.3.a) Volume of cement = **%0.4f m^3**" %C)
				st.write("7.3.b) Volume of water = **%0.4f m^3**" %W)
				st.write("7.3.c) Volume of 1st mineral admixture = **%0.4f m^3**" %Vl3)
				st.write("7.3.d) Volume of 1st mineral admixture = **%0.4f m^3**" %Vm3)
				st.write("7.3.e) Volume of 3rd mineral admixture = **%0.4f m^3**" %Vn3)
		st.write("7.4) Volume of chemical admixture (plasticiser) =**%0.4f m^3**" %P)
		st.write("7.5) Volume of all in one aggregate =**%0.4f m^3**" %G)
		st.write("Mass of coarse aggregate = **%d Kg**  " %MCA)
		st.write("Mass of fine aggregate = **%d Kg**" %MFA)
		st.write("****")

		st.write("**8] MIX PROPORTION FOR TRAIL 1**")
		if l==0 and m==0 and n==0:
			st.write("**8.1) CEMENT : %.3f Kg/m^3**" % Cement1)	
		else:
			if m==0 and n==0:
				st.write("**8.1.a) CEMENT (OPC) : %.3f Kg/m^2**" % Cement1)
				st.write("**8.1.b) 1st MINERAL ADMIXTURE CONTENT : %.3f Kg/m^3**" % l2)
			elif n==0:
				st.write("**8.1.a) CEMENT (OPC) : %.3f Kg/m^2**" % Cement1)
				st.write("**8.1.b) 1st MINERAL ADMIXTURE CONTENT : %.3f Kg/m^3**" % l2)
				st.write("**8.1.c) 2nd MINERAL ADMIXTURE CONTENT : %.3f Kg/m^3**" % m2)
				
			else:
				st.write("**8.1.a) CEMENT : %.3f Kg/m^2**" % Cement1)
				st.write("**8.1.b) 1st MINERAL ADMIXTURE CONTENT : %.3f Kg/m^3**" % l2)
				st.write("**8.1.c) 2nd MINERAL ADMIXTURE CONTENT : %.3f Kg/m^3**" % m2)
				st.write("**8.1.d) 3rd MINERAL ADMIXTURE CONTENT : %.3f Kg/m^3**" % n2)		
		st.write("**8.2)Water : %.4f Kg/m^3**" %water2)
		st.write("**8.3)Coarse aggregate(SSD) : %.4f Kg/m^3**" % MCA)
		st.write("**8.4)Fine aggregate (SSD): %.4f Kg/m^3**" % MFA)
		st.write("**8.5)Chemical admixture : %.4f Kg/m^3**" % P1)
		st.write("**8.6)Free water cementitious materials ratio : %.4f Kg/m^3**" % w_cmp)
		st.write("****")

		if FrMoCo1!=0 or FrMoCo2!=0:
			st.write("**Note**: Aggregates shall be used in saturated surface dry condition. If otherwise, when computing the requirement of mixing water, allowance shall be made for the free (surface) moisture contributed by the fine and coarse aggregates. On the other hand, if the aggregates are dry, the amount of mixing water shall be increased by an amount equal to the moisture likely to be absorbed by the aggregates. Necessary adjustments are also required to be made in mass of aggregates.")
			st.write("**TRAIL 2**")
			st.write("(*All in Kg/m^3*)")
			col1,col2,col3,col4=st.columns(4)
			col1.metric(label="**CEMENT**",value=Cement1)
			col2.metric(label="**WATER**",value=round(water22))

			if FrMoCo1<=0:
				col3.metric(label="**COARSE AGGREGATE(DRY)**",value=MCA1)
			elif FrMoCo1>0:
				col3.metric(label="**COARSE AGGREGATE(WET)**",value=MCA1)

			if FrMoCo2<=0:
				col4.metric(label="**FINE AGGREGATE(DRY)**",value=MFA1)
			elif FrMoCo2>0:
				col4.metric(label="**FINE AGGREGATE(WET)**",value=MFA1)
			if l==0 and m==0 and n==0:
				col1.metric(label="**CHEM.ADMIXTURE**",value=P1)
			else:
				if m==0 and n==0:
					col1,col2=st.columns(2)		
					col1.metric(label="**MIN.ADMIXTURE 1**",value=l2)
					col2.metric(label="**CHEM.ADMIXTURE**",value=P1)
				elif n==0:
					col1,col2,col3=st.columns(3)
					col1.metric(label="**MINERAL ADMIXTURE 1**",value=l2)
					col2.metric(label="**MINERAL ADMIXTURE 2**",value=m2)
					col3.metric(label="**CHEM.ADMIXTURE**",value=P1)
				else:
					col1,col2,col3,col4=st.columns(4)
					col1.metric(label="**MINERAL ADMIXTURE 1**",value=l2)
					col2.metric(label="**MINERAL ADMIXTURE 2**",value=m2)
					col3.metric(label="**MINERAL ADMIXTURE 3**",value=n2)
					col4.metric(label="**CHEM.ADMIXTURE**",value=P1)	
			col1.metric(label="**WATER-CEMENT RATIO**",value=round(w_cmp,4))
			
			st.write("***")	
			if FrMoCo1 != 0:
				if FrMoCo1<=0:
					st.write("Mass of coarse aggregate = **%d Kg**" %MCA)
					st.write("***Coarse aggregate is in dry condition***")
					st.write("Mass of coarse aggregate adjusted for dry condition = **%d Kg**" %MCA1)
				
				elif FrMoCo1>0:
					st.write("Mass of coarse aggregate = **%d Kg**" %MCA)
					st.write("***Coarse aggregate is in wet condition***")
					st.write("Mass of coarse aggregate adjusted for wet condition = **%d Kg**" %MCA1)
			if FrMoCo2 != 0:		
				if FrMoCo2<=0:
					st.write("Mass of fine aggregate = **%d Kg**" %MFA)
					st.write("***Fine aggregate is in dry condition***")
					st.write("Mass of Fine aggregate adjusted for dry condition = **%d Kg**" %MFA1)
				elif FrMoCo2>0:
					st.write("Mass of fine aggregate = **%d Kg**" %MFA)
					st.write("***Fine aggregate is in wet condition***")
					st.write("Mass of Fine aggregate adjusted for wet condition = **%d Kg**" %MFA1)

			st.write("**9]MIX PROPORTION AFTER ADJUSTMENT**")
			if l==0 and m==0 and n==0:
				st.write("**9.1) CEMENT : %.3f Kg/m^3**" % Cement1)	
			else:
				if m==0 and n==0:
					st.write("**9.1.a) CEMENT (OPC) : %.3f Kg/m^2**" % Cement1)
					st.write("**9.1.b) 1st MINERAL ADMIXTURE CONTENT : %.3f Kg/m^3**" % l2)
				elif n==0:
					st.write("**9.1.a) CEMENT (OPC) : %.3f Kg/m^2**" % Cement1)
					st.write("**9.1.b) 1st MINERAL ADMIXTURE CONTENT : %.3f Kg/m^3**" % l2)
					st.write("**9.1.c) 2nd MINERAL ADMIXTURE CONTENT : %.3f Kg/m^3**" % m2)
				
				else:
					st.write("**9.1.a) CEMENT : %.3f Kg/m^2**" % Cement1)
					st.write("**9.1.b) 1st MINERAL ADMIXTURE CONTENT : %.3f Kg/m^3**" % l2)
					st.write("**9.1.c) 2nd MINERAL ADMIXTURE CONTENT : %.3f Kg/m^3**" % m2)
					st.write("**9.1.d) 3rd MINERAL ADMIXTURE CONTENT : %.3f Kg/m^3**" % n2)		
			st.write("**9.2)Water : %.4f Kg/m^3**" %water22)
			if FrMoCo1<=0:
				st.write("**9.3)Coarse aggregate (dry) : %.4f Kg/m^3**" % MCA1)
			elif FrMoCo1>0:
				st.write("**9.3)Coarse aggregate (wet) : %.4f Kg/m^3**" % MCA1)
			if FrMoCo2<=0:	
				st.write("**9.4)Fine aggregate(dry): %.4f Kg/m^3**" % MFA1)
			elif FrMoCo2>0:
				st.write("**9.4)Fine aggregate (wet) : %.4f Kg/m^3**" % MFA1)
			st.write("**9.5)Chemical admixture : %.4f Kg/m^3**" % P1)
			st.write("**9.6)Free water cementitious materials ratio : %.4f Kg/m^3**" % w_cmp)


