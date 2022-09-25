from sre_constants import CATEGORY_NOT_LINEBREAK
import amino 
import numpy 

# Find R(f)
#input_sheet = open("./InputSheet", "r")
#lines = input_sheet.readlines()
#rfac = float(lines[0])/float(lines[1])
#input_sheet.close() 
amino_disp = input("Displacement of amino acid: ")
solvent_front = input("Solvent Front: ")
rfac = float(amino_disp)/float(solvent_front)
output_sheet = open("./OutputSheet.txt", "w")
output_sheet.writelines(f"{str(rfac)} \n")

# Round it
rounded_rfac = round(rfac, 2)
print(f"R(f): {rounded_rfac}")
output_sheet.writelines(f"{str(rounded_rfac)} \n")

# CHECK!
if (rounded_rfac == amino.amino_acid[0]): 
    print("crystine") 
    output_sheet.writelines(f"Crystine \n")

elif (rounded_rfac == amino.amino_acid[1]): 
    print("lysine")
    output_sheet.writelines(f"Lysine \n")

elif (rounded_rfac == amino.amino_acid[2]): 
    print("glycine")
    output_sheet.writelines(f"Glycine \n")

elif (rounded_rfac == amino.amino_acid[3]): 
    print("serine")
    output_sheet.writelines(f"Serine \n")

elif (rounded_rfac == amino.amino_acid[4]):
    print("alanine")
    output_sheet.writelines(f"Alanine \n")

elif (rounded_rfac == amino.amino_acid[5]): 
    print("proline") 
    output_sheet.writelines(f"Proline \n")

elif (rounded_rfac == amino.amino_acid[6]):
    print("valine")
    output_sheet.writelines(f"Valine \n")

elif (rounded_rfac == amino.amino_acid[7]):
    print("leucine")
    output_sheet.writelines(f"Leucine \n")

output_sheet.close()

     
        

