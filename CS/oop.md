# Object Oriented Programming

## Call-by-value vs Call-by-reference
#### Call-by-value :
- ***Copy*** of value is passed.
- Considered as ***local variable*** inside function.
#### Call-by-reference :
- ***Address*** of actual argument is passed.
- Caller's data can be modified by called function
- Specified by ***&*** in C++ - reference type.
  
## Overloading
- Same function name, different parameter lists, separate function definitions
- Allows same task performed on different data

## Aggregate data type
#### Array
- A collection of data of same type
- Elements are stored sequentially
#### Struct
- A collection of data of different types
#### Class
- Adds member ***functions***
- Combine data and functions into single unit -> ***object***
- Member variables and functions can be ***public / private***
- Constant call-by-reference params : More efficient than call-by-value
- Can ***inline*** very shor function def
- Static member variables : shared by all objects of a class

## Object Oriented Programming
- Encourages assembling complex programs out of similar components
  that can be designed and tested independently
- In OOP, program is made up of interacting components called ***objects***.
#### Principles of OOP
- Information hiding : Details of how operations work not known to user
- Data abstraction : Details of how data is manipulated within ADT/class
  not known to user
- Encapsulation : Bring together data and operations, but keep ***details*** hidden
#### Encapsulation
- Any data type includes ***Data*** and ***Operations***
#### Abstract Data Types(ADT)
- Programmers don't know details.
- Collection of data values together with set of basic operations defined for the values.
#### Public and private members
- Data in class almost always designated private in definition
    - Hide data from user
    - Allow manipulation only via operations (member functions)
- Public items are ***user-accessible***
#### Accessor and mutator functions (Getter & Setter)
- Call accessor member functions
    - Allow object to read data
    - Simple retrieval of member data
- Mutator member functions
    - Allow object to change data
    - Manipulated based on application
#### Constructors
- Initialization of objects : init some or all member variables. other actions
  possible as well
- A special kind of member function : automatically called when object declared
- Can overload constructors just like other functions

## Operator overloading
- Built-in operators can be overloaded to work with custom objects
- Friend function : not member function, has direct access to private members.
  Add eficiency only
- Operators can be overloaded as member functions

## Separate comilation
#### Class separation
- Class independence : separate class definition / implementation
- if implementation changes -> only that file need be changed
1. Interface file
    - Contains class definition with function and operator declarations / prototypes
    - Users ***see*** this
    - Separate compilation unit
2. Implementation file
    - Contains member function definitions
    - Separate compilation unit
#### Encapsulation
- Principle : separate how class is used by programmer from details of class's 
  implementation
1. All member variables should be private
2. Basic class operations should be : public member / friend functions, overloaded
   operators
3. Make class implementation unavailable to users of class
#### Class header files
- Class interface always in header file
- Programs that use the class will "include" it
#### Class implementation files
- Class inplementations in .cpp file
#### Building an executable file
- Source + Header file --(compile)--> object file + lib --(link)--> Run file

## Inheritance
- New class inherited from another class
- Base class
    - General class from which others derive
- Derived class
    - Automatically has base class's member variables / functions
    - Can add additional member functions and variables
- Can redefine member functions (inherited functions) with same parameters
  (Different from overloading)

## Polymorphism
- Refers to the ability to associate many meanings one function name by means of
  the late-binding mechanism.
- Polymorphism, late binding, virtual functions

## Template
- Function templates : define functions with parameter for a type
- Class templates : define class with parameter for subparts of class
- ex) c++ vector : vector\<int>