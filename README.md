```
   __          __  _   _    _____
   \ \        / / (_) | |  / ____|
    \ \  /\  / /   _  | | | |        ___
     \ \/  \/ /   | | | | | |       / _ \
      \  /\  /    | | | | | |____  | (_) |    W I L d c a r d   C O m p a r e   !
       \/  \/     |_| |_|  \_____|  \___/

                                                             By: Jecepede 'Weird' Al
```
With WilCo you can compare strings with the use of wildcards.


- - -


Explanation :

Hi and welcome to Python Script WilCo !  
When you have two string you want to compare but the first string, the givenString, has a changing field in it,
you can have this field be ignored in the compare by using the wildcard _ANY_ in the expected string.


- - -


Examples :

```
expectedString = "_ANY_ quick _ANY_ fox jumps over the lazy _ANY_ (and back)..."
```

The first \_ANY\_ could be 'A', 'The' etc  
The second \_ANY\_ could be basically any color. 'brown', 'red', 'blue' etc  
The last \_ANY\_ could be basically any animal. 'dog', 'fire ant', 'elephant' etc  

The givenString will be the same as the expectedString when...

```
givenString = "The quick brown fox jumps over the lazy dog (and back)..."                     True
givenString = "Some quick brown fox jumps over the lazy dog (and back)..."                    True
givenString = "The quick brown fox jumps over the lazy Carcharodon carcharias (and back)..."  True

givenString = "The fast brown fox jumps over the lazy dog (and back)..."                      False -> fast
givenString = "The quick brown fox is jumping over the lazy dog (and back)..."                False -> Jumping
givenString = "The quick brown fox jumps over the lazy dog (and back again)..."               False -> again
```


- - -


ToDo :

- A better way for displaying the differences

- The ability to give the wildcards a fixed length

  Example :

  ```
  givenString = "The quick brown fox jumps over the lazy dog (and back)..."
  expectedString = "The quick brown _ANY3_ jumps over the lazy dog (and back)..."
  ```

  'dog', 'ant' and other three letter animals are True
  'elephant' and other non three letter animals yield False

- When comparing for JSON or XML, field order does not matter  

  Example :

```
  <note>
     <to>Foo</to>
     <from>Bar</from>
  </note>
```

&nbsp;&nbsp;would be the same as :

```
  <note>
     <from>Bar</from>
     <to>Foo</to>
  </note>
```

- - -


Legal Mumbo Jumbo :

This softeware is published under  :
GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

In case you are wondering : WilCo is a nod to Roger Wilco from Space Quest ;-)

