grammar FormLang;

program     : form EOF ;
form        : 'form' STRING '{' field* '}' ;

field
    : textField
    | emailField
    | numberField
    | checkboxField
    | submitButton
    ;

textField       : 'text' STRING ;
emailField      : 'email' STRING ;
numberField     : 'number' STRING ;
checkboxField   : 'checkbox' STRING ;
submitButton    : 'submit' STRING ;

STRING : '"' ( ~["\\] | '\\' . )* '"' ;
WS      : [ \t\r\n]+ -> skip ;
