def valid(s):

    openstack = []
    starstack = []

    for i in range(len(s)):

        if s[i] == '(':
            openstack.append(i)

        elif s[i] == '*':
            starstack.append(i)

        elif s[i] == ')':

          
            if openstack:
                openstack.pop()

           
            elif starstack:
                starstack.pop()

            
            else:
                return False

    while openstack:

        if not starstack:
            return False

        if openstack[-1] > starstack[-1]:
            return False

        openstack.pop()
        starstack.pop()

    return True
print(valid("(*))"))

