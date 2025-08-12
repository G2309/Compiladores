from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from custom_types import IntType, FloatType, StringType, BoolType

class TypeCheckVisitor(SimpleLangVisitor):

  def visitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for * or /: {} and {}".format(left_type, right_type))

  def visitAddSub(self, ctx: SimpleLangParser.AddSubContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for + or -: {} and {}".format(left_type, right_type))
  
  def visitInt(self, ctx: SimpleLangParser.IntContext):
    return IntType()

  def visitFloat(self, ctx: SimpleLangParser.FloatContext):
    return FloatType()

  def visitString(self, ctx: SimpleLangParser.StringContext):
    return StringType()

  def visitBool(self, ctx: SimpleLangParser.BoolContext):
    return BoolType()

  def visitParens(self, ctx: SimpleLangParser.ParensContext):
    return self.visit(ctx.expr())
  from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from custom_types import IntType, FloatType, StringType, BoolType

class TypeCheckVisitor(SimpleLangVisitor):

  def visitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for * or /: {} and {}".format(left_type, right_type))

  def visitAddSub(self, ctx: SimpleLangParser.AddSubContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for + or -: {} and {}".format(left_type, right_type))
  
  def visitInt(self, ctx: SimpleLangParser.IntContext):
    return IntType()

  def visitFloat(self, ctx: SimpleLangParser.FloatContext):
    return FloatType()

  def visitString(self, ctx: SimpleLangParser.StringContext):
    return StringType()

  def visitBool(self, ctx: SimpleLangParser.BoolContext):
    return BoolType()

  def visitParens(self, ctx: SimpleLangParser.ParensContext):
    return self.visit(ctx.expr())

  # Como se menciona en el README, modificamos la gramatica añadiendo operaciones de módulo y potenciación, por lo que tambien
  # actualizamos y agregamos sus respectivas validaciones en el presente módulo
  
  # Funcion para analizar la operación módulo entre dos expresiones
  
  # Recibe un contexto del parser con la operacion modulo
  def visitMod(self, ctx: SimpleLangParser.ModContext):
      # obtenemos los operandos
      left_type = self.visit(ctx.expr(0))
      right_type = self.visit(ctx.expr(1))
      # Se verifica que sean enteros, 
      if isinstance(left_type, IntType) and isinstance(right_type, IntType):
          return IntType()
      else:
          raise TypeError(f"Unsupported operand types for %: {left_type} and {right_type}")
  
  # Funcion para analizar la potenciacion 
  
  # Recibe un contexto del parser con la operacion potencia
  def visitPow(self, ctx: SimpleLangParser.PowContext):
      # se reciben los operandos, base y exponente
      left_type = self.visit(ctx.expr(0))
      right_type = self.visit(ctx.expr(1))
      # se verifica si son enteros o floats
      if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
          return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
      else:
          raise TypeError(f"Unsupported operand types for ^: {left_type} and {right_type}")
  
  # funcion para analizar comparadores: <, >, >=, <=
  def visitCompare(self, ctx: SimpleLangParser.CompareContext):
      # se reciben los operandos, base y exponente
      left = self.visit(ctx.expr(0))
      right = self.visit(ctx.expr(1))
      # C: comparadores < > solo para numéricos
      if isinstance(left, (IntType, FloatType)) and isinstance(right, (IntType, FloatType)):
        return BoolType()
      raise TypeError(f"Unsupported operand types for {ctx.op.text}: {left} and {right}")
