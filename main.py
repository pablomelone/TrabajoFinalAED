import visualizacion as vis
import validacion as val
import logica as log

__author__ = 'TP4-G003 | Olivero Aimaretti, Alexis Ivan - Legajo 89.348 - Comisión 1K13'
__author__ = 'TP4-G003 | Costamagna, Maria Paz - Legajo 89.978 - Comisión 1K7'
__author__ = 'TP4-G003 | Melone, Pablo A. - Legajo 90.429 - Comisión 1K13'
__author__ = 'TP4-G003 | Torres, Aylen - Legajo 93.696 - Comisión 1K13'


def main():
    op = 0
    v = []
    matriz_rating = []
    while op != '8':

        op = vis.menu()

        if op == '1':
            v = log.cargar_archivo()
        
        elif len(v) == 0 and op in '2345':

            print("\nNo hay registros cargados")

        elif op == '2':
            tipo_busqueda = val.validacion_opcion_busqueda()

            if tipo_busqueda == 1:
                parametro_busqueda = val.validar_carga_isbn()
            elif tipo_busqueda == 2:
                parametro_busqueda = val.validar_carga_titulo()
            else:
                parametro_busqueda = None

            if parametro_busqueda is None:
                pass
            else:
                pos_libro_buscado = log.busqueda_libro(v, tipo_busqueda, parametro_busqueda)

                if pos_libro_buscado is None:
                    print("El libro no ha sido encontrado, reintente con otro valor.")
                else:
                    v[pos_libro_buscado].revisiones += 1

                    print(" ")
                    print("="*120)
                    print(" "*50+"¡Libro Encontrado!")
                    print("="*120)

                    vis.print_libro(v[pos_libro_buscado])

        elif op == '3':
            libro_mayor_revisiones = log.mayor_revisiones(v)
            promedio_rating_idioma = log.rating_promedio_idioma(v,libro_mayor_revisiones)
            
            print("")
            print("="*120)
            print(" "*50+"El libro con mayores revisiones es:")
            print("="*120)

            vis.print_libro(libro_mayor_revisiones)

            if libro_mayor_revisiones.rating > promedio_rating_idioma:
                print("\nEl libro tiene un rating superior al promedio de su idioma")
            elif libro_mayor_revisiones.rating < promedio_rating_idioma:
                print("\nEl libro tiene un rating inferior al promedio de su idioma")
            elif libro_mayor_revisiones.rating == promedio_rating_idioma:
                print("\nEl libro tiene un rating igual al promedio de su idioma")


        elif op == '4':
            array_filtrado = log.array_filtrado_por_rango(v)
            matriz_rating = log.generar_matriz_popular(array_filtrado)
            print("\n¡Matriz generada correctamente!")

        elif op == '5':
            publicacion_decada, mayor = log.contador_decadas(v)
            vis.mostrar_libros_por_decada(publicacion_decada)
            vis.mayor_por_decada(publicacion_decada, mayor)

        elif len(matriz_rating) == 0 and op in '6':
            print("\nLa matriz no ha sido generada. Reintente")

        elif op == '6':
            total_registros = log.generar_archivo(matriz_rating)
            print(f'¡Archivo generado correctamente! La cantidad de registros guardados fue de {total_registros}.')

        elif op == '7':
            array_guardado = log.cargar_archivo_binario()
            if array_guardado is None:
                print('\nEl archivo no ha sido creado aun.')
            else:
                vis.mostrar_libros(array_guardado)

        elif op == '8':

            print('¡Adios!')

        else:
            print("Opcion ingresada incorrecta. Reintente.")


if __name__ == '__main__':
    main()
