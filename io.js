const lysine = 0.14;
const glycine = 0.26;
const serine = 0.27;
const alanine = 0.38; 
const proline = 0.43; 
const valine = 0.60;
const leucine = 0.73; 

function check(rf) {
    if (lysine == rf) {
        return "lysine";
    }
    if (glycine == rf) {
        return "glycine";
    }
    if (serine == rf) {
        return "serine";
    }
    if (alanine == rf) {
        return "alanine";
    }
    if (proline == rf) {
        return "proline";
    }
    if (valine == rf) {
        return "valine";
    }
    if (leucine == rf) {
        return "leucine"
    }
    else {return "Unknown"}
}

function display() 
{
   var amino_acid = Number(document.getElementById("amino_acid").value);
   var solvent_front = Number(document.getElementById("solvent_front").value);
   var retardation_factor = amino_acid/solvent_front;
   var retardation_factor_rounded = retardation_factor.toFixed(2) 
   document.write("The R(f) is " + retardation_factor_rounded + "<br>"); 
   alert("For the nerds: R(f) = " + String(retardation_factor));
   document.write("The amino acid is " + check(retardation_factor_rounded));
   return retardation_factor_rounded;
}

