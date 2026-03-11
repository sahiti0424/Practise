import numpy as np
import matplotlib.pyplot as plt
#derivatives
def f(x):
    return x**2
def df(x):
    return 2*x
#by linspace we create equally spaced points between -5 and 5
x_values=np.linspace(-5,5,100)
y_values=f(x_values)
dy_values=df(x_values)
print(f"f(3) = {f(3)}")
print(f"f'(3) = {df(3)}")
print(f"f(-2) = {f(-2)}")        
print(f"f'(-2) = {df(-2)}")  

#plotting
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function f(x)')
plt.plot(x_values, y_values, label='f(x)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("derivatives.png")
plt.show()

#gradient descent-finding minimum of a function, minimize loss function
def gradient_descent(start_x,learning_rate,steps):
    x=start_x
    history=[x]
    
    for i in range(steps):
        grad=df(x) #calculate slope
        x=x-learning_rate*grad #move against the slope
        history.append(x)

        if i % 10 == 0:
            print(f"Step {i:3d}: x = {x:.4f}, f(x) = {f(x):.4f}")

    return x, history

print("\nGradient Descent finding minimum of f(x) = x²:")
print("Starting at x = 4.0")
final_x, history = gradient_descent(start_x=4.0,
    learning_rate=0.1, steps=50)
print(f"\nFinal x: {final_x:.6f}")
print(f"Minimum value: {f(final_x):.6f}")
print("Expected minimum: x=0, f(x)=0")

# Plot gradient descent path
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x_values, y_values, color="blue", label="f(x) = x²")
history_y = [f(x) for x in history]
plt.scatter(history, history_y, color="red", s=30, zorder=5)
plt.plot(history, history_y, color="red", alpha=0.5, label="GD path")
plt.title("Gradient Descent on f(x) = x²")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(range(len(history)), [f(x) for x in history], color="green")
plt.title("Loss decreasing over steps")
plt.xlabel("Step")
plt.ylabel("f(x) = Loss")
plt.grid(True)

plt.tight_layout()
plt.savefig("gradient_descent.png")
plt.show()

#chain rule
def y(x):
    return (3*x + 2) ** 2

def dy(x):
    return 6 * (3*x + 2)   # chain rule result

x_vals = np.linspace(-3, 3, 100)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y(x_vals), color="blue", label="y = (3x+2)²")
plt.plot(x_vals, dy(x_vals), color="red", label="dy/dx = 6(3x+2)")
plt.title("Chain Rule Example")
plt.xlabel("x")
plt.legend()
plt.grid(True)
plt.savefig("chain_rule.png")
plt.show()

#Partial Derivatives
def loss(w1, w2):
    return w1**2 + w2**2   # simple loss function

def dloss_dw1(w1):
    return 2 * w1   # partial derivative w.r.t w1

def dloss_dw2(w2):
    return 2 * w2   # partial derivative w.r.t w2

w1, w2 = 3.0, 4.0
print(f"Loss at w1={w1}, w2={w2}: {loss(w1, w2)}")
print(f"∂loss/∂w1 = {dloss_dw1(w1)}")
print(f"∂loss/∂w2 = {dloss_dw2(w2)}")
print("These gradients tell us how to update each weight!")

#learning rate effect
# Too high LR = overshoots minimum
# Too low LR = takes forever
# Just right = converges nicely

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, lr, title in zip(axes,
        [0.01, 0.1, 0.9],
        ["Too Small (lr=0.01)", "Just Right (lr=0.1)", "Too Large (lr=0.9)"]):

    _, history = gradient_descent(4.0, lr, 50)
    loss_history = [f(x) for x in history]

    ax.plot(loss_history, color="blue")
    ax.set_title(title)
    ax.set_xlabel("Steps")
    ax.set_ylabel("Loss")
    ax.grid(True)

plt.tight_layout()
plt.savefig("learning_rates.png")
plt.show()