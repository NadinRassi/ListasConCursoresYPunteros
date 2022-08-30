// Ordena la lista. Ordena los strings sencible a Mayusculas y Minusculas
Procedure Lista.Sort(Ascendente: Boolean);
    Var 
        P, Q: PosicionLista;
        X1, X2: TipoElemento;
    Begin
        // Ordeno por metodo de burbuja
        P := Inicio;
        While P <> Nulo Do Begin
            Q := Inicio;
            While Q <> Nulo Do begin
                X1 := Cursor[Q].Datos;
                If Siguiente(Q) <> Nulo Then Begin
                    X2 := Cursor[Cursor[Q].Prox].Datos;
                    if Ascendente then
                        if X1.Clave > X2.Clave then
                            Intercambio(Q, Cursor[Q].Prox);
                    if Not Ascendente then
                        if X1.Clave < X2.Clave then
                            Intercambio(Q, Cursor[Q].Prox);
                End;
                Q := Cursor[Q].Prox;
            End;
            P := Cursor[P].Prox;
        End;
    End;

Function Lista.Comienzo: PosicionLista;
    Begin
        Comienzo := Inicio;
    End;

Function Lista.Fin: PosicionLista;
    Begin
        Fin := Final;
    End;

