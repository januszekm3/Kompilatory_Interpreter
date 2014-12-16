ttype = {}

ttype['+'] = {}
ttype['+']['int'] = {}
ttype['+']['int']['int'] = 'int'
ttype['+']['int']['float'] = 'float'
ttype['+']['int']['string'] = 'error'
ttype['+']['int']['error'] = 'error'

ttype['+']['float'] = {}
ttype['+']['float']['int'] = 'float'
ttype['+']['float']['float'] = 'float'
ttype['+']['float']['string'] = 'error'
ttype['+']['float']['error'] = 'error'

ttype['+']['string'] = {}
ttype['+']['string']['int'] = 'error'
ttype['+']['string']['float'] = 'error'
ttype['+']['string']['string'] = 'error'
ttype['+']['string']['error'] = 'error'

ttype['+']['error'] = {}
ttype['+']['error']['int'] = 'error'
ttype['+']['error']['float'] = 'error'
ttype['+']['error']['string'] = 'error'
ttype['+']['error']['error'] = 'error'


ttype['-'] = {}
ttype['-']['int'] = {}
ttype['-']['int']['int'] = 'int'
ttype['-']['int']['float'] = 'float'
ttype['-']['int']['string'] = 'error'
ttype['-']['int']['error'] = 'error'

ttype['-']['float'] = {}
ttype['-']['float']['int'] = 'float'
ttype['-']['float']['float'] = 'float'
ttype['-']['float']['string'] = 'error'
ttype['-']['float']['error'] = 'error'

ttype['-']['string'] = {}
ttype['-']['string']['int'] = 'error'
ttype['-']['string']['float'] = 'error'
ttype['-']['string']['string'] = 'error'
ttype['-']['string']['error'] = 'error'

ttype['-']['error'] = {}
ttype['-']['error']['int'] = 'error'
ttype['-']['error']['float'] = 'error'
ttype['-']['error']['string'] = 'error'
ttype['-']['error']['error'] = 'error'


ttype['*'] = {}
ttype['*']['int'] = {}
ttype['*']['int']['int'] = 'int'
ttype['*']['int']['float'] = 'float'
ttype['*']['int']['string'] = 'error'
ttype['*']['int']['error'] = 'error'

ttype['*']['float'] = {}
ttype['*']['float']['int'] = 'float'
ttype['*']['float']['float'] = 'float'
ttype['*']['float']['string'] = 'error'
ttype['*']['float']['error'] = 'error'

ttype['*']['string'] = {}
ttype['*']['string']['int'] = 'string'
ttype['*']['string']['float'] = 'error'
ttype['*']['string']['string'] = 'error'
ttype['*']['string']['error'] = 'error'

ttype['*']['error'] = {}
ttype['*']['error']['int'] = 'error'
ttype['*']['error']['float'] = 'error'
ttype['*']['error']['string'] = 'error'
ttype['*']['error']['error'] = 'error'


ttype['/'] = {}
ttype['/']['int'] = {}
ttype['/']['int']['int'] = 'int'
ttype['/']['int']['float'] = 'float'
ttype['/']['int']['string'] = 'error'
ttype['/']['int']['error'] = 'error'

ttype['/']['float'] = {}
ttype['/']['float']['int'] = 'float'
ttype['/']['float']['float'] = 'float'
ttype['/']['float']['string'] = 'error'
ttype['/']['float']['error'] = 'error'

ttype['/']['string'] = {}
ttype['/']['string']['int'] = 'error'
ttype['/']['string']['float'] = 'error'
ttype['/']['string']['string'] = 'error'
ttype['/']['string']['error'] = 'error'

ttype['/']['error'] = {}
ttype['/']['error']['int'] = 'error'
ttype['/']['error']['float'] = 'error'
ttype['/']['error']['string'] = 'error'
ttype['/']['error']['error'] = 'error'


ttype['%'] = {}
ttype['%']['int'] = {}
ttype['%']['int']['int'] = 'int'
ttype['%']['int']['float'] = 'error'
ttype['%']['int']['string'] = 'error'
ttype['%']['int']['error'] = 'error'

ttype['%']['float'] = {}
ttype['%']['float']['int'] = 'error'
ttype['%']['float']['float'] = 'error'
ttype['%']['float']['string'] = 'error'
ttype['%']['float']['error'] = 'error'

ttype['%']['string'] = {}
ttype['%']['string']['int'] = 'error'
ttype['%']['string']['float'] = 'error'
ttype['%']['string']['string'] = 'error'
ttype['%']['string']['error'] = 'error'

ttype['%']['error'] = {}
ttype['%']['error']['int'] = 'error'
ttype['%']['error']['float'] = 'error'
ttype['%']['error']['string'] = 'error'
ttype['%']['error']['error'] = 'error'


ttype['|'] = {}
ttype['|']['int'] = {}
ttype['|']['int']['int'] = 'int'
ttype['|']['int']['float'] = 'error'
ttype['|']['int']['string'] = 'error'
ttype['|']['int']['error'] = 'error'

ttype['|']['float'] = {}
ttype['|']['float']['int'] = 'error'
ttype['|']['float']['float'] = 'error'
ttype['|']['float']['string'] = 'error'
ttype['|']['float']['error'] = 'error'

ttype['|']['string'] = {}
ttype['|']['string']['int'] = 'error'
ttype['|']['string']['float'] = 'error'
ttype['|']['string']['string'] = 'error'
ttype['|']['string']['error'] = 'error'

ttype['|']['error'] = {}
ttype['|']['error']['int'] = 'error'
ttype['|']['error']['float'] = 'error'
ttype['|']['error']['string'] = 'error'
ttype['|']['error']['error'] = 'error'


ttype['&'] = {}
ttype['&']['int'] = {}
ttype['&']['int']['int'] = 'int'
ttype['&']['int']['float'] = 'error'
ttype['&']['int']['string'] = 'error'
ttype['&']['int']['error'] = 'error'

ttype['&']['float'] = {}
ttype['&']['float']['int'] = 'error'
ttype['&']['float']['float'] = 'error'
ttype['&']['float']['string'] = 'error'
ttype['&']['float']['error'] = 'error'

ttype['&']['string'] = {}
ttype['&']['string']['int'] = 'error'
ttype['&']['string']['float'] = 'error'
ttype['&']['string']['string'] = 'error'
ttype['&']['string']['error'] = 'error'

ttype['&']['error'] = {}
ttype['&']['error']['int'] = 'error'
ttype['&']['error']['float'] = 'error'
ttype['&']['error']['string'] = 'error'
ttype['&']['error']['error'] = 'error'


ttype['^'] = {}
ttype['^']['int'] = {}
ttype['^']['int']['int'] = 'int'
ttype['^']['int']['float'] = 'error'
ttype['^']['int']['string'] = 'error'
ttype['^']['int']['error'] = 'error'

ttype['^']['float'] = {}
ttype['^']['float']['int'] = 'error'
ttype['^']['float']['float'] = 'error'
ttype['^']['float']['string'] = 'error'
ttype['^']['float']['error'] = 'error'

ttype['^']['string'] = {}
ttype['^']['string']['int'] = 'error'
ttype['^']['string']['float'] = 'error'
ttype['^']['string']['string'] = 'error'
ttype['^']['string']['error'] = 'error'

ttype['^']['error'] = {}
ttype['^']['error']['int'] = 'error'
ttype['^']['error']['float'] = 'error'
ttype['^']['error']['string'] = 'error'
ttype['^']['error']['error'] = 'error'


ttype['&&'] = {}
ttype['&&']['int'] = {}
ttype['&&']['int']['int'] = 'int'
ttype['&&']['int']['float'] = 'int'
ttype['&&']['int']['string'] = 'int'
ttype['&&']['int']['error'] = 'error'

ttype['&&']['float'] = {}
ttype['&&']['float']['int'] = 'int'
ttype['&&']['float']['float'] = 'int'
ttype['&&']['float']['string'] = 'int'
ttype['&&']['float']['error'] = 'error'

ttype['&&']['string'] = {}
ttype['&&']['string']['int'] = 'int'
ttype['&&']['string']['float'] = 'int'
ttype['&&']['string']['string'] = 'int'
ttype['&&']['string']['error'] = 'error'

ttype['&&']['error'] = {}
ttype['&&']['error']['int'] = 'error'
ttype['&&']['error']['float'] = 'error'
ttype['&&']['error']['string'] = 'error'
ttype['&&']['error']['error'] = 'error'


ttype['||'] = {}
ttype['||']['int'] = {}
ttype['||']['int']['int'] = 'int'
ttype['||']['int']['float'] = 'int'
ttype['||']['int']['string'] = 'int'
ttype['||']['int']['error'] = 'error'

ttype['||']['float'] = {}
ttype['||']['float']['int'] = 'int'
ttype['||']['float']['float'] = 'int'
ttype['||']['float']['string'] = 'int'
ttype['||']['float']['error'] = 'error'

ttype['||']['string'] = {}
ttype['||']['string']['int'] = 'int'
ttype['||']['string']['float'] = 'int'
ttype['||']['string']['string'] = 'int'
ttype['||']['string']['error'] = 'error'

ttype['||']['error'] = {}
ttype['||']['error']['int'] = 'error'
ttype['||']['error']['float'] = 'error'
ttype['||']['error']['string'] = 'error'
ttype['||']['error']['error'] = 'error'


ttype['>>'] = {}
ttype['>>']['int'] = {}
ttype['>>']['int']['int'] = 'int'
ttype['>>']['int']['float'] = 'error'
ttype['>>']['int']['string'] = 'error'
ttype['>>']['int']['error'] = 'error'

ttype['>>']['float'] = {}
ttype['>>']['float']['int'] = 'error'
ttype['>>']['float']['float'] = 'error'
ttype['>>']['float']['string'] = 'error'
ttype['>>']['float']['error'] = 'error'

ttype['>>']['string'] = {}
ttype['>>']['string']['int'] = 'error'
ttype['>>']['string']['float'] = 'error'
ttype['>>']['string']['string'] = 'error'
ttype['>>']['string']['error'] = 'error'

ttype['>>']['error'] = {}
ttype['>>']['error']['int'] = 'error'
ttype['>>']['error']['float'] = 'error'
ttype['>>']['error']['string'] = 'error'
ttype['>>']['error']['error'] = 'error'


ttype['<<'] = {}
ttype['<<']['int'] = {}
ttype['<<']['int']['int'] = 'int'
ttype['<<']['int']['float'] = 'error'
ttype['<<']['int']['string'] = 'error'
ttype['<<']['int']['error'] = 'error'

ttype['<<']['float'] = {}
ttype['<<']['float']['int'] = 'error'
ttype['<<']['float']['float'] = 'error'
ttype['<<']['float']['string'] = 'error'
ttype['<<']['float']['error'] = 'error'

ttype['<<']['string'] = {}
ttype['<<']['string']['int'] = 'error'
ttype['<<']['string']['float'] = 'error'
ttype['<<']['string']['string'] = 'error'
ttype['<<']['string']['error'] = 'error'

ttype['<<']['error'] = {}
ttype['<<']['error']['int'] = 'error'
ttype['<<']['error']['float'] = 'error'
ttype['<<']['error']['string'] = 'error'
ttype['<<']['error']['error'] = 'error'


ttype['=='] = {}
ttype['==']['int'] = {}
ttype['==']['int']['int'] = 'int'
ttype['==']['int']['float'] = 'int'
ttype['==']['int']['string'] = 'error'
ttype['==']['int']['error'] = 'error'

ttype['==']['float'] = {}
ttype['==']['float']['int'] = 'int'
ttype['==']['float']['float'] = 'int'
ttype['==']['float']['string'] = 'error'
ttype['==']['float']['error'] = 'error'

ttype['==']['string'] = {}
ttype['==']['string']['int'] = 'error'
ttype['==']['string']['float'] = 'error'
ttype['==']['string']['string'] = 'int'
ttype['==']['string']['error'] = 'error'

ttype['==']['error'] = {}
ttype['==']['error']['int'] = 'error'
ttype['==']['error']['float'] = 'error'
ttype['==']['error']['string'] = 'error'
ttype['==']['error']['error'] = 'error'


ttype['!='] = {}
ttype['!=']['int'] = {}
ttype['!=']['int']['int'] = 'int'
ttype['!=']['int']['float'] = 'int'
ttype['!=']['int']['string'] = 'error'
ttype['!=']['int']['error'] = 'error'

ttype['!=']['float'] = {}
ttype['!=']['float']['int'] = 'int'
ttype['!=']['float']['float'] = 'int'
ttype['!=']['float']['string'] = 'error'
ttype['!=']['float']['error'] = 'error'

ttype['!=']['string'] = {}
ttype['!=']['string']['int'] = 'error'
ttype['!=']['string']['float'] = 'error'
ttype['!=']['string']['string'] = 'int'
ttype['!=']['string']['error'] = 'error'

ttype['!=']['error'] = {}
ttype['!=']['error']['int'] = 'error'
ttype['!=']['error']['float'] = 'error'
ttype['!=']['error']['string'] = 'error'
ttype['!=']['error']['error'] = 'error'

ttype['<'] = {}
ttype['<']['int'] = {}
ttype['<']['int']['int'] = 'int'
ttype['<']['int']['float'] = 'int'
ttype['<']['int']['string'] = 'error'
ttype['<']['int']['error'] = 'error'

ttype['<']['float'] = {}
ttype['<']['float']['int'] = 'int'
ttype['<']['float']['float'] = 'int'
ttype['<']['float']['string'] = 'error'
ttype['<']['float']['error'] = 'error'

ttype['<']['string'] = {}
ttype['<']['string']['int'] = 'error'
ttype['<']['string']['float'] = 'error'
ttype['<']['string']['string'] = 'int'
ttype['<']['string']['error'] = 'error'

ttype['<']['error'] = {}
ttype['<']['error']['int'] = 'error'
ttype['<']['error']['float'] = 'error'
ttype['<']['error']['string'] = 'error'
ttype['<']['error']['error'] = 'error'


ttype['<='] = {}
ttype['<=']['int'] = {}
ttype['<=']['int']['int'] = 'int'
ttype['<=']['int']['float'] = 'int'
ttype['<=']['int']['string'] = 'error'
ttype['<=']['int']['error'] = 'error'

ttype['<=']['float'] = {}
ttype['<=']['float']['int'] = 'int'
ttype['<=']['float']['float'] = 'int'
ttype['<=']['float']['string'] = 'error'
ttype['<=']['float']['error'] = 'error'

ttype['<=']['string'] = {}
ttype['<=']['string']['int'] = 'error'
ttype['<=']['string']['float'] = 'error'
ttype['<=']['string']['string'] = 'int'
ttype['<=']['string']['error'] = 'error'

ttype['<=']['error'] = {}
ttype['<=']['error']['int'] = 'error'
ttype['<=']['error']['float'] = 'error'
ttype['<=']['error']['string'] = 'error'
ttype['<=']['error']['error'] = 'error'


ttype['>'] = {}
ttype['>']['int'] = {}
ttype['>']['int']['int'] = 'int'
ttype['>']['int']['float'] = 'int'
ttype['>']['int']['string'] = 'error'
ttype['>']['int']['error'] = 'error'

ttype['>']['float'] = {}
ttype['>']['float']['int'] = 'int'
ttype['>']['float']['float'] = 'int'
ttype['>']['float']['string'] = 'error'
ttype['>']['float']['error'] = 'error'

ttype['>']['string'] = {}
ttype['>']['string']['int'] = 'error'
ttype['>']['string']['float'] = 'error'
ttype['>']['string']['string'] = 'int'
ttype['>']['string']['error'] = 'error'

ttype['>']['error'] = {}
ttype['>']['error']['int'] = 'error'
ttype['>']['error']['float'] = 'error'
ttype['>']['error']['string'] = 'error'
ttype['>']['error']['error'] = 'error'


ttype['>='] = {}
ttype['>=']['int'] = {}
ttype['>=']['int']['int'] = 'int'
ttype['>=']['int']['float'] = 'int'
ttype['>=']['int']['string'] = 'error'
ttype['>=']['int']['error'] = 'error'

ttype['>=']['float'] = {}
ttype['>=']['float']['int'] = 'int'
ttype['>=']['float']['float'] = 'int'
ttype['>=']['float']['string'] = 'error'
ttype['>=']['float']['error'] = 'error'

ttype['>=']['string'] = {}
ttype['>=']['string']['int'] = 'error'
ttype['>=']['string']['float'] = 'error'
ttype['>=']['string']['string'] = 'int'
ttype['>=']['string']['error'] = 'error'

ttype['>=']['error'] = {}
ttype['>=']['error']['int'] = 'error'
ttype['>=']['error']['float'] = 'error'
ttype['>=']['error']['string'] = 'error'
ttype['>=']['error']['error'] = 'error'
