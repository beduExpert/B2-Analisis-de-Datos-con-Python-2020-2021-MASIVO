def verificar_resultados(df, porcentaje_1, porcentaje_2, porcentaje_3):
    diameter_column = 'estimated_diameter.meters.estimated_diameter_max'
    mean = df[diameter_column].mean()
    std = df[diameter_column].std()
    
    p1 = df[(df[diameter_column] >= (mean - std)) & (df[diameter_column] <= (mean + std))].shape[0] * 100 / df.shape[0]
    if round(p1, 6) != round(porcentaje_1, 6):
        print(f'El porcentaje a 1 desviación estándar no fue calculado correctamente.')
        print(f'Porcentaje esperado: {round(p1, 6)}; Porcentaje recibido: {round(porcentaje_1, 6)}')

    p2 = df[(df[diameter_column] >= (mean - 2 * std)) & (df[diameter_column] <= (mean + 2 * std))].shape[0] * 100 / df.shape[0]
    if round(p2, 6) != round(porcentaje_2, 6):
        print(f'El porcentaje a 2 desviaciones estándar no fue calculado correctamente.')
        print(f'Porcentaje esperado: {round(p2, 6)}; Porcentaje recibido: {round(porcentaje_2, 6)}')

    p3 = df[(df[diameter_column] >= (mean - 3 * std)) & (df[diameter_column] <= (mean + 3 * std))].shape[0] * 100 / df.shape[0]
    if round(p3, 6) != round(porcentaje_3, 6):
        print(f'El porcentaje a 3 desviaciones estándar no fue calculado correctamente.')
        print(f'Porcentaje esperado: {round(p3, 6)}; Porcentaje recibido: {round(porcentaje_3, 6)}')
