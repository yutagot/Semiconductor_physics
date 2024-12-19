.. _basic_equation:

Basic equations
=========================================

In this section, we introduce some basic equations related to semiconductor devices.

.. contents:: Index 

Poisson equation
-----------------

The electrostatic potential can be calculated with the corresponding charge distribution :math:`\rho` with Poisson equation.

.. math::
   :label: poisson

   \nabla \cdot \left(\varepsilon_s \nabla\Psi\right) = -\rho,

where :math:`\varepsilon_s` is the dielectric permittivity and :math:`\varepsilon_s = 11.9 \varepsilon_0` for Si.
:math:`\Psi` is the electrostatic potential.
The electric charge density in a semiconductor is given by the summation of the electron charge density :math:`n`, the hole charge density :math:`p`, and the ionized impurity doping density :math:`D`.
Therefore, 

.. math::
   :label: electric_charge

   \rho = q(n - p + D),

where :math:`q` is the elementary charge.
Note that :math:`D` consists of the ionized acceptor and donor type impurity densities, which mean :math:`D = N_A - N_D`.

Thus, :eq:`poisson` can be expressed as following,

.. math::
   :label: poisson_electric_charge

   \nabla^2\Psi = -\frac{q(n - p + N_A - N_D)}{\varepsilon_s}.

The left side can be rewritten in the orthogonal coordinate system, 

.. math::
   :label: nabla_squared_psi

   \nabla^2\Psi(x, y, z) = \frac{\partial^2\Psi}{\partial x^2} + \frac{\partial^2\Psi}{\partial y^2} + \frac{\partial^2\Psi}{\partial z^2}.
 
For a 1D problem, :eq:`nabla_squared_psi` can be reduced to 

.. math::
   :label: poisson_one_dimensional

   \frac{d^2\Psi_i}{d x^2} = -\frac{d\xi}{dx} = -\frac{\rho}{\varepsilon_s} =  -\frac{q(n - p + N_A - N_D)}{\varepsilon_s},
 
Of course, :math:`\xi = - \nabla\Psi` holds in :eq:`poisson_one_dimensional`.

Poisson equation is often used to determine the distributions of electrostatic potential and electric field caused by a charge density :math:`\rho`.

Current-density equations
----------------------------

The common current equation consists of the drift component, caused by the electric field, and the diffusion component, caused by the gradient of the carrier concentration.
The current density equations are below,

.. math::
   :label: electron_current

   \mathbf{J_n} = q\mu_nn\xi + qD_n\nabla n,

.. math::
   :label: hole_current

   \mathbf{J_p} = q\mu_pp\xi - qD_p\nabla p

and

.. math::
   :label: total_current

   \mathbf{J_{conduction}} = \mathbf{J_n} + \mathbf{J_p},

where :math:`\mathbf{J_n}` and :math:`\mathbf{J_p}` are the electron and hole current densities, respectively.
:math:`\mu_n` and :math:`\mu_ p` are the electron and hole mobilities.
For nondegenerate semiconductors, the carrier diffusion constants (:math:`D_n` and :math:`D_p`) and the mobilities are given by the Einstein relation,

.. math::
   :label: electron_diffusion

   D_n = \frac{kT}{q}\mu_n,

.. math::
   :label: hole_diffusion

   D_p = \frac{kT}{q}\mu_p.

Therefore, for a 1D case, :eq:`electron_current` and :eq:`hole_current` can be reduced to 

.. math::
   :label: electron_current_quasi_fermi

   J_n = q\mu_nn\xi + qD_n\frac{dn}{dx} = q\mu_n\left(n\xi + \frac{kT}{q}\frac{dn}{dx}\right) = \mu_nn\frac{dE_{Fn}}{dx},

and

.. math::
   :label: hole_current_quasi_fermi

   J_p = q\mu_pp\xi - qD_p\frac{dp}{dx} = q\mu_p\left(p\xi - \frac{kT}{q}\frac{dp}{dx}\right) = \mu_pp\frac{dE_{Fp}}{dx},

where :math:`E_{Fn}` and :math:`E_{Fp}` are quasi Fermi levels for electrons and holes, respectively.

These equations indicate that no electron or hole current run in the region where the quasi Fermi level is constant over x.
Note that these equations are valid for low electric field :math:`\xi`.
If the electric field is sufficiently high, the term :math:`\mu_n\xi` or :math:`\mu_p\xi` should be replaced by the saturation velocity :math:`v_s`.
The last equalities about :math:`E_{Fn}` and :math:`E_{Fp}` do not hold any more either.

Continuity equations
----------------------------

While the above current-density equations hold for steady-state conditions, the continuity equations deal with time-dependent states such as low-level injection, generation, and recombination.
You can see :ref:`generation_and_recombination` for further information about recombination and generation.
The net change of carrier concentration is the difference between generation and recombination, plus the net current flowing in and out of the region of interest.

.. math::
   :label: electron_current_continuity

   \frac{\partial n}{\partial t} = G_n - U_n + \frac{1}{q}\nabla \cdot \mathbf{J_n},

.. math::
   :label: hole_current_continuity

   \frac{\partial n}{\partial t} = G_n - U_n + \frac{1}{q}\nabla \cdot \mathbf{J_n},

where :math:`G_n` and :math:`G_p` are the electron and hole generation rate (:math:`\mathrm{cm}^{-3}\mathrm{s}^{-1}`), respectively.
:math:`U_n` and :math:`U_p` are the electron and hole recombination rate (:math:`\mathrm{cm}^{-3}\mathrm{s}^{-1}`), which have the following relations,

.. math::
   :label: electron_recombination_lifetime

   U_n = \frac{\Delta n}{\tau_n},


.. math::
   :label: hole_recombination_lifetime

   U_p = \frac{\Delta p}{\tau_p}.



For more details, refer to :cite:`sze2006`.

.. bibliography::
   :style: plain


last update: |today|