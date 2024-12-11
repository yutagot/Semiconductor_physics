Basic equations
=========================================

In this section, we introduce some basic equations related to semiconductor devices.

.. contents:: Index 

Poisson equation
-----------------

The electrostatic potential can be calculated with the corresponding charge distribution :math:`\rho` with Poisson equation.

.. math::

   \nabla \cdot \left(\varepsilon_s \nabla\Psi\right) = -\rho,\tag{1}

where :math:`\varepsilon_s` is the dielectric permittivity and :math:`\varepsilon_s = 11.9 \varepsilon_0` for Si.
:math:`\Psi` is the electrostatic potential.
The electric charge density in a semiconductor is given by the summation of the electron charge density :math:`n`, the hole charge density :math:`p`, and the ionized impurity doping density :math:`D`.
Therefore, 

.. math::

   \rho = q(n - p + D),\tag{2}

where :math:`q` is the elementary charge.
Note that :math:`D` consists of the ionized acceptor and donor type impurity densities, which mean :math:`D = N_A - N_D`.

Thus, Eq. 1 can be expressed as following,

.. math::

   \nabla^2\Psi = -\frac{q(n - p + N_A - N_D)}{\varepsilon_s}\tag{3}.

The left side can be rewritten in the orthogonal coordinate system, 

.. math::

   \nabla^2\Psi(x, y, z) = \frac{\partial^2\Psi}{\partial x^2} + \frac{\partial^2\Psi}{\partial y^2} + \frac{\partial^2\Psi}{\partial z^2}\tag{4}.
 
For a 1D problem, Eq. 4 can be reduced to 

.. math::

   \frac{d^2\Psi_i}{d x^2} = -\frac{d\xi}{dx} = -\frac{\rho}{\varepsilon_s} =  -\frac{q(n - p + N_A - N_D)}{\varepsilon_s},\tag{5}
 
Of course, :math:`\xi = - \nabla\Psi` holds in Eq. 5.

Poisson equation is often used to determine the distributions of electrostatic potential and electric field caused by a charge density :math:`\rho`.

Current-density equations
----------------------------

The common current equation consists of the drift component, caused by the electric field, and the diffusion component, caused by the gradient of the carrier concentration.
The current density equations are below,

.. math::

  \mathbf{J_n} = q\mu_nn\xi + qD_n\nabla n,\tag{6}

.. math::

   \mathbf{J_p} = q\mu_pp\xi - qD_p\nabla p,\tag{7}

and

.. math::

   \mathbf{J_{conduction}} = \mathbf{J_n} + \mathbf{J_p},\tag{8}

where :math:`\mathbf{J_n}` and :math:`\mathbf{J_p}` are the electron and hole current densities, respectively.
:math:`\mu_n` and :math:`\mu_ p` are the electron and hole mobilities.
For nondegenerate semiconductors, the carrier diffusion constants (:math:`D_n` and :math:`D_p`) and the mobilities are given by the Einstein relation,

.. math::

   D_n = \frac{kT}{q}\mu_n,\tag{9}

.. math::

   D_p = \frac{kT}{q}\mu_p.\tag{10}

Therefore, for a 1D case, Eqs. 6 and 7 can be reduced to 

.. math::

   J_n = q\mu_nn\xi + qD_n\frac{dn}{dx} = q\mu_n\left(n\xi + \frac{kT}{q}\frac{dn}{dx}\right) = \mu_nn\frac{dE_{Fn}}{dx},\tag{11}

and

.. math::

   J_p = q\mu_pp\xi - qD_p\frac{dp}{dx} = q\mu_p\left(p\xi - \frac{kT}{q}\frac{dp}{dx}\right) = \mu_pp\frac{dE_{Fp}}{dx},\tag{12}

where :math:`E_{Fn}` and :math:`E_{Fp}` are quasi Fermi levels for electrons and holes, respectively.

Note that these equations are valid for low electric field :math:`\xi`.
If the electric field is sufficiently high, the term :math:`\mu_n\xi` or :math:`\mu_p\xi` should be replaced by the saturation velocity :math:`v_s`.
The last equalities about :math:`E_{Fn}` and :math:`E_{Fp}` do not hold any more either.

Continuity equations
----------------------------

While the above current-density equations hold for steady-state conditions, the continuity equations deal with time-dependent states such as low-level injection, generation, and recombination.