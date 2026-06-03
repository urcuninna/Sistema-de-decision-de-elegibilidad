# Sistema de Decision de Elegibilidad

## Objetivo del sistema

Clasificar empleados para:

- Remote Work Eligibility
- Performance Bonus Eligibility
- Leadership Program Eligibility
- Wellness Support Program Eligibility
- Education Benefit Eligibility

## Reglas del negocio

### REGLA 1 — Remote Work Eligibility

Contexto real; la empresa tiene política híbrida, ya que no todos los cargos aplican.

Reglas.

Empleado puede aplicar si:

✔ cargo permite remoto. AND ✔ mínimo 6 meses de antigüedad. AND ✔ aprobación del líder. AND ✔ sin sanciones disciplinarias activas.

### REGLA 2 — Performance Bonus Eligibility

Contexto Colombia. Muchas empresas manejan bonificación variable por desempeño.

Reglas.

Elegible si:

✔ contrato indefinido o fijo. AND ✔ desempeño >=4.0. AND ✔ mínimo 12 meses antigüedad.

### REGLA 3 — Leadership Program Eligibility

Programa interno de liderazgo.

Reglas.

Elegible si:

✔ desempeño >=4.5. AND ✔ engagement >=80. AND ✔ sin sanciones. OR ✔ manager nomination=True.

## REGLA 4 — Wellness Support Program

MUY RH real.

Programa bienestar que puede incluir:

- apoyo psicológico
- manejo estrés
- wellbeing coaching.

Reglas.

Elegible si:

✔ stress_level >=8 OR ✔ engagement <60. OR ✔ manager referral=True.

### REGLA 5 — Education Benefit Eligibility

Inspirado en beneficios corporativos reales. Apoyo económico para estudios.

Reglas.

Elegible si:

✔ contrato indefinido. AND ✔ mínimo 1 año antigüedad. AND ✔ desempeño >=4. AND ✔ programa relacionado con el cargo.