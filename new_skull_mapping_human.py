import math

def distance_formula(p_1,p_2):
    distance = (((p_1[0] - p_2[0]) ** 2) + ((p_1[1] - p_2[1]) ** 2) + ((p_1[2] - p_2[2]) ** 2)) ** (1/2)
    return (distance)

def fourth_point_finder_without_checker(a_1,b_1,c_1,ad,bd,cd):
    ab = distance_formula(a_1,b_1)
    ac = distance_formula(a_1,c_1)
    bc = distance_formula(c_1,b_1)
    
    #the following point transitions are to make life easier
    #point a is moved to the origin and all other points are subsequently moved across a vector -a_1
    a_2 = [0,0,0]
    b_2 = [b_1[0] - a_1[0], b_1[1] - a_1[1], b_1[2] - a_1[2]]
    c_2 = [c_1[0] - a_1[0], c_1[1] - a_1[1], c_1[2] - a_1[2]]

    #point b is then rotated to align with the x-axis which causes a subsequent rotation for points c and d along the y and z axis
    b_3 = [distance_formula(a_1,b_1),0,0]
    b_3_z_rotation = math.atan(-b_2[1]/b_2[0])
    b_3_intermediate = [b_2[0] * math.cos(b_3_z_rotation) - b_2[1] * math.sin(b_3_z_rotation),0,b_2[2]] #works
    b_3_y_rotation = math.atan(b_3_intermediate[2]/b_3_intermediate[0])
    c_3_intermediate = [c_2[0] * math.cos(b_3_z_rotation) - c_2[1] * math.sin(b_3_z_rotation),c_2[0] * math.sin(b_3_z_rotation) + c_2[1] * math.cos(b_3_z_rotation),c_2[2]] #works
    c_3 = [c_3_intermediate[0] * math.cos(b_3_y_rotation) + c_3_intermediate[2] * math.sin(b_3_y_rotation), c_3_intermediate[1], -c_3_intermediate[0] * math.sin(b_3_y_rotation) + c_3_intermediate[2] * math.cos(b_3_y_rotation)] #works
    
    #point c is then rotated around the x-axis so that it is on the x-y-plane (z = 0)
    c_4_x_rotation = math.atan(-c_3[2]/c_3[1])
    c_4 = [c_3[0], c_3[1] * math.cos(c_4_x_rotation) - c_3[2] * math.sin(c_4_x_rotation), 0] #works

    #this is the check
    print(ab,ac,bc)
    print(distance_formula(a_2,b_3), distance_formula(a_2,c_4), distance_formula(b_3,c_4))


    #rotations and transitions are complete for now
    d_x = (-(ad ** 2) - (b_3[0] ** 2) + (bd ** 2))/(-2 * b_3[0])
    d_y = ((cd ** 2) - (ad ** 2) - (c_4[1] ** 2) - (c_4[0] ** 2) + (2 * d_x * c_4[0]))/(-2 * c_4[1])
    d_z = ((ad ** 2) - (d_y ** 2) - (d_x ** 2)) ** (1/2) #can be possitive or negative to give two point
    d_1 = [d_x,d_y,d_z] #works (d_z can have negative sign put in front of it)
    d_3_versions = []
    for x in range (2):
        d_1[2] = d_1[2] * (-1 ** x) #to account for both placements of the fourth point
        #now need to rotate and transition back
        d_2_intermediate_1 = [d_1[0], d_1[1] * math.cos(-c_4_x_rotation) - d_1[2] * math.sin(-c_4_x_rotation), d_1[1] * math.sin(-c_4_x_rotation) + d_1[2] * math.cos(-c_4_x_rotation)] #rotates it opposite of the previous point c rotation around the x axis
        d_2_intermediate_2 = [d_2_intermediate_1[0] * math.cos(-b_3_y_rotation) + d_2_intermediate_1[2] * math.sin(-b_3_y_rotation), d_2_intermediate_1[1], -d_2_intermediate_1[0] * math.sin(-b_3_y_rotation) + d_2_intermediate_1[2] * math.cos(-b_3_y_rotation)] #rotates it opposite of the previous point b rotation around the y axis
        d_2 = [d_2_intermediate_2[0] * math.cos(-b_3_z_rotation) - d_2_intermediate_2[1] * math.sin(-b_3_z_rotation), d_2_intermediate_2[0] * math.sin(-b_3_z_rotation) + d_2_intermediate_2[1] * math.cos(-b_3_z_rotation), d_2_intermediate_2[2]] #rotates it opposite of the previous point b rotation around the z axis
        d_3 = [d_2[0] + a_1[0],d_2[1] + a_1[1],d_2[2] + a_1[2]] #moves point d back up to where it was before point a was moved to the origin
        #works
        d_3_versions.append(d_3)
    print(d_3_versions)
    return(d_3_versions[0])

def fourth_point_finder_with_checker(a_1,b_1,c_1,ad,bd,cd,checker_point,checker_distance):
    ab = distance_formula(a_1,b_1)
    ac = distance_formula(a_1,c_1)
    bc = distance_formula(c_1,b_1)
    
    #the following point transitions are to make life easier
    #point a is moved to the origin and all other points are subsequently moved across a vector -a_1
    a_2 = [0,0,0]
    b_2 = [b_1[0] - a_1[0], b_1[1] - a_1[1], b_1[2] - a_1[2]]
    c_2 = [c_1[0] - a_1[0], c_1[1] - a_1[1], c_1[2] - a_1[2]]

    #point b is then rotated to align with the x-axis which causes a subsequent rotation for points c and d along the y and z axis
    b_3 = [distance_formula(a_1,b_1),0,0]
    b_3_z_rotation = math.atan(-b_2[1]/b_2[0])
    b_3_intermediate = [b_2[0] * math.cos(b_3_z_rotation) - b_2[1] * math.sin(b_3_z_rotation),0,b_2[2]] #works
    b_3_y_rotation = math.atan(b_3_intermediate[2]/b_3_intermediate[0])
    c_3_intermediate = [c_2[0] * math.cos(b_3_z_rotation) - c_2[1] * math.sin(b_3_z_rotation),c_2[0] * math.sin(b_3_z_rotation) + c_2[1] * math.cos(b_3_z_rotation),c_2[2]] #works
    c_3 = [c_3_intermediate[0] * math.cos(b_3_y_rotation) + c_3_intermediate[2] * math.sin(b_3_y_rotation), c_3_intermediate[1], -c_3_intermediate[0] * math.sin(b_3_y_rotation) + c_3_intermediate[2] * math.cos(b_3_y_rotation)] #works
    
    #point c is then rotated around the x-axis so that it is on the x-y-plane (z = 0)
    c_4_x_rotation = math.atan(-c_3[2]/c_3[1])
    c_4 = [c_3[0], c_3[1] * math.cos(c_4_x_rotation) - c_3[2] * math.sin(c_4_x_rotation), 0] #works

    #this is the check
    print(ab,ac,bc)
    print(distance_formula(a_2,b_3), distance_formula(a_2,c_4), distance_formula(b_3,c_4))


    #rotations and transitions are complete for now
    d_x = (-(ad ** 2) - (b_3[0] ** 2) + (bd ** 2))/(-2 * b_3[0])
    d_y = ((cd ** 2) - (ad ** 2) - (c_4[1] ** 2) - (c_4[0] ** 2) + (2 * d_x * c_4[0]))/(-2 * c_4[1])
    d_z = ((ad ** 2) - (d_y ** 2) - (d_x ** 2)) ** (1/2) #can be possitive or negative to give two point
    d_1 = [d_x,d_y,d_z] #works (d_z can have negative sign put in front of it)
    d_3_versions = []
    for x in range (2):
        d_1[2] = d_1[2] * (-1 ** x) #to account for both placements of the fourth point
        #now need to rotate and transition back
        d_2_intermediate_1 = [d_1[0], d_1[1] * math.cos(-c_4_x_rotation) - d_1[2] * math.sin(-c_4_x_rotation), d_1[1] * math.sin(-c_4_x_rotation) + d_1[2] * math.cos(-c_4_x_rotation)] #rotates it opposite of the previous point c rotation around the x axis
        d_2_intermediate_2 = [d_2_intermediate_1[0] * math.cos(-b_3_y_rotation) + d_2_intermediate_1[2] * math.sin(-b_3_y_rotation), d_2_intermediate_1[1], -d_2_intermediate_1[0] * math.sin(-b_3_y_rotation) + d_2_intermediate_1[2] * math.cos(-b_3_y_rotation)] #rotates it opposite of the previous point b rotation around the y axis
        d_2 = [d_2_intermediate_2[0] * math.cos(-b_3_z_rotation) - d_2_intermediate_2[1] * math.sin(-b_3_z_rotation), d_2_intermediate_2[0] * math.sin(-b_3_z_rotation) + d_2_intermediate_2[1] * math.cos(-b_3_z_rotation), d_2_intermediate_2[2]] #rotates it opposite of the previous point b rotation around the z axis
        d_3 = [d_2[0] + a_1[0],d_2[1] + a_1[1],d_2[2] + a_1[2]] #moves point d back up to where it was before point a was moved to the origin
        #works
        d_3_versions.append(d_3)
    print(d_3_versions)
    #to get an estimate of which of the two points recieved is more accurate, they are both tested with the distance formula with a known point and distance (the checkers)
    check_0 = (distance_formula(d_3_versions[0],checker_point) - checker_distance) ** 2
    check_1 = (distance_formula(d_3_versions[0],checker_point) - checker_distance) ** 2
    if check_0 > check_1:
        return(d_3_versions[0])
    else:
        return(d_3_versions[1])

#alpha is the frontal-sphenoid-parietal junction(s)
#beta is the temporal-parietal-occipital junction(s)
#gamma is the temporal-zygomatic suture's most lateral point(s)

l = [0,0,0] #lambda (it's the origin)
l_b = 11.5 #lambda to bregma
l_e = 17.0 #lambda to bridge of nose
l_f = 8.3 #lambda to foramen magnum
l_be = 8.7 #lambda to beta
l_al = 13.0 #lambda to alpha
l_ga = 0.0 #lambda to gamma
l_t = 19.6 #lambda to upper incisors "gap"

b_e = 10.3 #bregma to bridge of nose
b_f = 13.8 #bregma to foramen magnum
b_be = 12.2 #bregma to beta
b_al = 8.4 #bregma to alpha
b_ga = 0.0 #bregma to gamma
b_t = 15.9 #bregma to upper incisors "gap"

e_f = 13.5 #bridge of nose to foramen magnum
e_be = 13.5 #bridge of nose to beta
e_al = 7.2 #bridge of nose to alpha
e_ga = 0.0 #bridge of nose to gamma
e_t = 6.5 #bridge of nose to upper incisors "gap"

f_be = 7.1 #foramen magnum to beta
f_al = 11.4 #foramen magnum to alpha

be_be = 11.5 #beta to beta
al_al = 10.2 #alpha to alpha
ga_ga = 0.0 #gamma to gamma

general_height = 13.1 #the general height of the skull as the distance between two parallel lines where one passes through the foramen magnum and the other through the bregma
st = 0.5 #skull thickness

integrate_skull_thickness = False #isn't good for actually mapping, just good for brain volume

if integrate_skull_thickness == True:
    be_be -= (2 * st) #beta to beta
    al_al -= (2 * st) #alpha to alpha
    l_b -= (2 * st) #lambda to bregma
    l_e -= (2 * st) #lambda to bridge of nose
    l_f -= (2 * st) #lambda to foramen magnum
    l_be -= (2 * st) #lambda to beta
    l_al -= (2 * st) #lambda to alpha
    b_e -= (2 * st) #bregma to bridge of nose
    b_f -= (2 * st) #bregma to foramen magnum
    b_be -= (2 * st) #bregma to beta
    b_al -= (2 * st) #bregma to alpha
    e_f -= (2 * st) #bridge of nose to foramen magnum
    e_be -= (2 * st) #bridge of nose to beta
    e_al -= (2 * st) #bridge of nose to alpha
    general_height -= (2 * st) #the general height of the skull as the distance between two parallel lines where one passes through the foramen magnum and the other through the bregma
    

e = [l_e, 0, 0] #bridge of nose

def triangular_coordinates(d_1,d_2): #2D with lambda as point 1 and bridge of nose as point 2, d_1 is from lambda and d_2 is from the bridge of nose
    x_value = ((d_2 ** 2) - (d_1 ** 2) - (l_e ** 2)) / (-2 * l_e)
    y_value = ((d_1 ** 2) - (x_value ** 2)) ** (1/2)
    return ([x_value, y_value, 0])

f = triangular_coordinates(l_f,e_f) #foramen magnum
if f[1] >= 0: #because there are two possible points where the foramen magnum can exist with the given information (one above and one below the x-axis), we move it to the one below
    f[1] = -f[1]

b = triangular_coordinates(l_b,b_e) #bregma
if b[1] <= 0:
    b[1] = -b[1]

#the alpha and beta point mapping assumes that the skull is symetrical along the sagittal plane

a_1 = fourth_point_finder_without_checker(l,e,b,l_al,e_al,b_al) #alpha on the positive side of the z-axis
if a_1[2] <= 0:
    a_1[2] = -a_1[2]
a_2 = [a_1[0],a_1[1],-a_1[2]]  #alpha on the negative side of the z-axis 

b_1 = fourth_point_finder_without_checker(l,e,b,l_be,e_be,b_be) #beta on the positive side of the z-axis
if b_1[2] <= 0:
    b_1[2] = -b_1[2]
b_2 = [b_1[0],b_1[1],-b_1[2]] #beta on the negative side of the z-axis 

t = triangular_coordinates(l_t,e_t)
if t[1] >= 0:
    t[1] = -t[1]

if integrate_skull_thickness == True: #needs to be active for brain volume calculations
    lower_bound_skull_volume = (((1/2) * l_e * b[1]) + ((1/2) * l_e * -f[1])) * (b_1[2] + a_1[2]) #the sume of the triangle above the x-axis (bregma lambda nose-bridge) and below the x-axis (foramen lambda nose-bridge) times the mean skull width
    print(lower_bound_skull_volume)
    upper_bound_skull_volume = (general_height * l_e) * (b_1[2] + a_1[2])
    print(upper_bound_skull_volume)
    average = (lower_bound_skull_volume + upper_bound_skull_volume) / 2
    print(average, "cc is the estimated brain volume")
else: #if skull thickness is turned off then the angles/mapping can be on
    def angle_finder(a,b,c): #finds the angle formed by line ab and bc
        line_a = distance_formula(b,c)
        line_b = distance_formula(a,c)
        line_c = distance_formula(a,b)
        angle_b = math.acos(((line_a**2) + (line_c**2) - (line_b**2))/(2*line_a*line_c)) #law of cosines
        return(math.degrees(angle_b))

    biped_angle = angle_finder(e,l,f) #foramen magnum positioning
    prog_angle = angle_finder(t,e,[e[0],t[1],0]) #the angle of which the upper mandible juts out from the "imaginary forehead line"
    forehead_angle = angle_finder(l,e,b)
    top_head_angle = angle_finder(l,b,e)
    back_width_angle = angle_finder(b_1,l,b_2)
    front_width_angle = angle_finder(a_1,l,a_2)
    width_index = al_al/be_be
    projection_angle = angle_finder(l,e,t)
    print(biped_angle,
    prog_angle,
    forehead_angle,
    top_head_angle,
    back_width_angle,
    front_width_angle,
    width_index,
    projection_angle,)
    print(distance_formula(f,t))

def print_coordinates():
    print (l,"lambda \n",e,"nose bridge \n",b,"bregma \n",f,"foramen magnum \n",t,"upper incisor gap \n",a_1,"alpha \n",b_2,"beta")

print_coordinates()

#error finder below
total_errors = []
r_t = 0 #this is the running total
total_errors.append([abs(l_b - distance_formula(l,b)), "lambda to bregma"])
total_errors.append([abs(l_e - distance_formula(l,e)), "lambda to nose bridge"])
total_errors.append([abs(l_f - distance_formula(l,f)), "lambda to foramen magnum"])
total_errors.append([abs(l_be - distance_formula(l,b_1)), "lambda to beta"])
total_errors.append([abs(l_al - distance_formula(l,a_1)), "lambda to alpha"])
total_errors.append([abs(l_t - distance_formula(l,t)), "lambda to upper incisor diastema"])

total_errors.append([abs(b_e - distance_formula(b,e)), "bregma to nose bridge"])
total_errors.append([abs(b_f - distance_formula(b,f)), "bregma to foramen magnum"])
total_errors.append([abs(b_be - distance_formula(b,b_1)), "bregma to beta"])
total_errors.append([abs(b_al - distance_formula(b,a_1)), "bregma to alpha"])
total_errors.append([abs(b_t - distance_formula(b,t)), "bregma to upper incisor diastema"])

total_errors.append([abs(e_f - distance_formula(e,f)), "bridge of nose to foramen magnum"])
total_errors.append([abs(e_be - distance_formula(e,b_1)), "bridge of nose to beta"])
total_errors.append([abs(e_al - distance_formula(e,a_1)), "bridge of nose to alpha"])
total_errors.append([abs(e_t - distance_formula(e,t)), "bridge of nose to upper incisor diastema"])

total_errors.append([abs(f_be - distance_formula(f,b_1)), "foramen magnum to beta"])
total_errors.append([abs(f_al - distance_formula(f,a_1)), "foramen magnum to alpha"])

total_errors.append([abs(be_be - distance_formula(b_1,b_2)), "beta to beta"])
total_errors.append([abs(al_al - distance_formula(a_1,a_2)), "alpha to alpha"])

for a in total_errors:
    r_t += a[0]
print(r_t/len(total_errors), "average error in cm off")
    
maximum = 0
max_measurement = ""
for b in total_errors:
    if b[0] > maximum:
        maximum = b[0]
        max_measurement = b[1]
print(maximum,max_measurement, "largest error in cm off")
print(total_errors)