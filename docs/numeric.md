# Numerical Methods & Analysis

## 1. Overview

This project compares several numerical integration methods for simulating charged particle motion in an electric field.

The goal is to evaluate each method in terms of:

* accuracy
* stability
* energy conservation

---

## 2. Equations of Motion

The particle dynamics are governed by:

$$
\frac{d\mathbf{r}}{dt} = \mathbf{v}, \quad
\frac{d\mathbf{v}}{dt} = \frac{q}{m} \mathbf{E}(\mathbf{r})
$$

This system is solved numerically using different integration schemes.

---

## 3. Euler Method

The Euler method is the simplest numerical integrator:

$$
x_{n+1} = x_n + v_n dt
$$

$$
v_{n+1} = v_n + a_n dt
$$

### Characteristics

* First-order accuracy
* Simple and fast
* Poor stability for long simulations

### Observation

Euler tends to accumulate error quickly, especially in regions with strong electric fields.

---

## 4. Runge–Kutta 4 (RK4)

RK4 improves accuracy by evaluating intermediate slopes.

### Characteristics

* Fourth-order accuracy
* High precision per timestep
* Computationally more expensive

### Observation

RK4 produces smooth and accurate trajectories, but does not conserve energy over long time periods.

---

## 5. Velocity Verlet

Velocity Verlet is widely used in physics simulations.

### Characteristics

* Second-order accuracy
* Time-reversible
* Better energy conservation than RK4

### Observation

Provides a good balance between accuracy and stability, especially for conservative systems.

---

## 6. Boris Method

The Boris algorithm is specifically designed for charged particle motion in electromagnetic fields.

### Characteristics

* Symplectic method
* Excellent energy conservation
* Stable for long simulations

### Observation

Even though originally designed for magnetic fields, it remains stable and robust in this simulation framework.

---

## 7. Energy Analysis

The accuracy of each method is evaluated using total energy:

$$
E = K + U = \frac{1}{2}mv^2 + qV
$$

Energy error is defined as:

$$
\Delta E(t) = |E(t) - E(0)|
$$

### Key Insight

* Euler → large energy drift
* RK4 → small short-term error, but accumulates over time
* Verlet → better long-term stability
* Boris → best energy conservation

---

