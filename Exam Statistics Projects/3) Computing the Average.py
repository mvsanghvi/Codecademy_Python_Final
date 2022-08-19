grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_average(grades_input):
  grades_sum=0
  for i in grades_input:
    grades_sum+=i
    grades_average=grades_sum/float(len(grades_input))
  return grades_average

print(grades_average(grades))