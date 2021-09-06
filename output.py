weight = 20 / 2.205
dosage = weight * 30
weight = round(weight)

print("CORRECT DOSAGE")
print("For a patient weighing {:.1f} kg,".format(round(weight)))
print("  the correct dosage is {: .2f} mg the first day".format(round(dosage, 2)))
