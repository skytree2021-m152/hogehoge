def Johnny(mag,score):
    if score>=0.25:
        image="https://3.bp.blogspot.com/-lzZsNV3zWuw/U7O66Xv-z3I/AAAAAAAAiVE/sUbsC_xKdP8/s800/whiteman3_tehe.png"
        return image
    elif score<=-0.25:
        image="https://2.bp.blogspot.com/-jb-vJs48VBs/U7O64nt6_SI/AAAAAAAAiUg/N46UerPXEJU/s800/whiteman2_shock.png"
        return image
    else:
        if mag>=10:
            image="https://2.bp.blogspot.com/-Bb6rSSRE9u4/U7O648vJ9oI/AAAAAAAAiUk/DpmLgnnSOZU/s800/whiteman2_surprise.png"
            return image
        elif mag>=5:
            image="https://1.bp.blogspot.com/-Zg12XWQzTQA/U7O64KmAGhI/AAAAAAAAiUY/PvNni1PWTyk/s800/whiteman2_idea.png"
            return image
        elif mag>=0.5:
            image="https://4.bp.blogspot.com/-a9lMcx1MMoA/U7O65959olI/AAAAAAAAiVA/_0H9lqeSebU/s800/whiteman3_question.png"
            return image
        else:
            image="https://1.bp.blogspot.com/-5QISGE_PCrE/U7O659adahI/AAAAAAAAiU8/IseeWCzoMOA/s800/whiteman3_sleep.png"
            return image
    