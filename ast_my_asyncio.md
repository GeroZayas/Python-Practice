Module(
   body=[
      Import(
         names=[
            alias(name='asyncio')]),
      AsyncFunctionDef(
         name='hello_world',
         args=arguments(),
         body=[
            Expr(
               value=Call(
                  func=Name(id='print', ctx=Load()),
                  args=[
                     Constant(value='Hello')])),
            Expr(
               value=Await(
                  value=Call(
                     func=Attribute(
                        value=Name(id='asyncio', ctx=Load()),
                        attr='sleep',
                        ctx=Load()),
                     args=[
                        Constant(value=2)]))),
            Expr(
               value=Call(
                  func=Name(id='print', ctx=Load()),
                  args=[
                     Constant(value='World!')]))]),
      AsyncFunctionDef(
         name='square',
         args=arguments(
            args=[
               arg(arg='x')]),
         body=[
            Expr(
               value=Await(
                  value=Call(
                     func=Attribute(
                        value=Name(id='asyncio', ctx=Load()),
                        attr='sleep',
                        ctx=Load()),
                     args=[
                        Constant(value=1)]))),
            Expr(
               value=Call(
                  func=Name(id='print', ctx=Load()),
                  args=[
                     BinOp(
                        left=Name(id='x', ctx=Load()),
                        op=Pow(),
                        right=Constant(value=2))]))]),
      AsyncFunctionDef(
         name='main',
         args=arguments(),
         body=[
            Expr(
               value=Await(
                  value=Call(
                     func=Attribute(
                        value=Name(id='asyncio', ctx=Load()),
                        attr='gather',
                        ctx=Load()),
                     args=[
                        Call(
                           func=Name(id='hello_world', ctx=Load())),
                        Call(
                           func=Name(id='square', ctx=Load()),
                           args=[
                              Constant(value=8)])])))]),
      Expr(
         value=Call(
            func=Attribute(
               value=Name(id='asyncio', ctx=Load()),
               attr='run',
               ctx=Load()),
            args=[
               Call(
                  func=Name(id='main', ctx=Load()))])),
      Expr(
         value=Call(
            func=Name(id='input', ctx=Load()),
            args=[
               Constant(value='Hit ENTER to exit')]))])
