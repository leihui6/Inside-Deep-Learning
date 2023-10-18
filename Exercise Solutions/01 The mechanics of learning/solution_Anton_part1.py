>>> for _ in range(15):
...     opt.zero_grad()
...     loss = f(p[0], p[1])
...     loss.backward()
...     opt.step()
...     print(p, loss)
... 
Parameter containing:
tensor([1.1800, 9.0200], requires_grad=True) tensor(96.0508, grad_fn=<AddBackward0>)
Parameter containing:
tensor([1.9640, 8.2360], requires_grad=True) tensor(61.5039, grad_fn=<AddBackward0>)
Parameter containing:
tensor([2.5912, 7.6088], requires_grad=True) tensor(39.3976, grad_fn=<AddBackward0>)
Parameter containing:
tensor([3.0930, 7.1070], requires_grad=True) tensor(25.2285, grad_fn=<AddBackward0>)
Parameter containing:
tensor([3.4944, 6.7056], requires_grad=True) tensor(16.1750, grad_fn=<AddBackward0>)
Parameter containing:
tensor([3.8155, 6.3845], requires_grad=True) tensor(10.4215, grad_fn=<AddBackward0>)
Parameter containing:
tensor([4.0724, 6.1276], requires_grad=True) tensor(6.8235, grad_fn=<AddBackward0>)
Parameter containing:
tensor([4.2779, 5.9221], requires_grad=True) tensor(4.6744, grad_fn=<AddBackward0>)
Parameter containing:
tensor([4.4423, 5.7577], requires_grad=True) tensor(3.5456, grad_fn=<AddBackward0>)
Parameter containing:
tensor([4.5739, 5.6261], requires_grad=True) tensor(3.1933, grad_fn=<AddBackward0>)
Parameter containing:
tensor([4.6791, 5.5209], requires_grad=True) tensor(3.5159, grad_fn=<AddBackward0>)
Parameter containing:
tensor([4.7633, 5.4367], requires_grad=True) tensor(4.5403, grad_fn=<AddBackward0>)
Parameter containing:
tensor([4.8306, 5.3694], requires_grad=True) tensor(6.4316, grad_fn=<AddBackward0>)
Parameter containing:
tensor([4.8845, 5.3155], requires_grad=True) tensor(9.5257, grad_fn=<AddBackward0>)
Parameter containing:
tensor([4.9276, 5.2724], requires_grad=True) tensor(14.3954, grad_fn=<AddBackward0>)