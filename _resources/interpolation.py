class interpolation:
    # one dimensional 
    # pt1 must be left most point
    def linear_interpolation(self, pt1, pt2, unknown):
        xy = 0
        val = 1
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        #Write your code for linear interpolation here
        pt1_xy = pt1[xy]
        pt1_val = pt1[val]
        pt2_xy = pt2[xy]
        pt2_val = pt2[val]

        len_21 = pt2_xy - pt1_xy
        weight_pt2 = pt2_val * (pt2_xy - unknown)
        weight_pt1 = pt1_val * (unknown - pt1_xy)

        return int( (weight_pt1 + weight_pt2) / len_21 )

    # two dimensional 
    # pt1,pt2,pt3,pt4 = LIST[x,y,val]
    # (pt1 top left going clockwise)
    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        x = 0
        y = 1
        val = 2
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""
        
        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task
        weight_r1 = self.linear_interpolation([pt4[x], pt4[val]], [pt3[x], pt3[val]], unknown[x])
        weight_r2 = self.linear_interpolation([pt1[x], pt1[val]], [pt2[x], pt2[val]], unknown[x])

        weight_p = self.linear_interpolation([pt4[y], weight_r2], [pt1[y], weight_r1], unknown[y])

        return weight_p

