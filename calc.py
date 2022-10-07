import amino

def retardation(amino_acid_displcaement, solvent_front): 
    retardation_factor = amino_acid_displcaement/solvent_front
    return retardation_factor

def checkamino(rounded_rfac): 
    # CHECK!
    if (rounded_rfac == amino.amino_acid[0]): 
        print("crystine") 
        return "Crystine"

    elif (rounded_rfac == amino.amino_acid[1]): 
        print("lysine")
        return "Lysine"

    elif (rounded_rfac == amino.amino_acid[2]): 
        print("glycine")
        return "Glycine"

    elif (rounded_rfac == amino.amino_acid[3]): 
        print("serine")
        return "Serine"

    elif (rounded_rfac == amino.amino_acid[4]):
        print("alanine")
        return "Alanine"

    elif (rounded_rfac == amino.amino_acid[5]): 
        print("proline") 
        return "Proline"

    elif (rounded_rfac == amino.amino_acid[6]):
        print("valine")
        return "Valine"

    elif (rounded_rfac == amino.amino_acid[7]):
        print("leucine")
        return "Leucine"

   
