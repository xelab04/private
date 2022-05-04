Module HelloWorld
    Sub Main()
        Dim array() As integer = {5,1,4,2,8}
        Dim temp As integer
        Dim change As boolean = true

        while change
            change = false
            for i = 0 to array.Length-2
                if (array(i) > array(i+1)) then
                change = true
                    temp = array(i)
                    array(i) = array(i+1)
                    array(i+1) = temp
                end if
            next
        end while
    
        for i = 0 to array.Length-1
        
            Console.Writeline(array(i))
        next
    end Sub
end Module
