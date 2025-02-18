# **ER Diagram Explanation – Zoo Management System**

## **1. Introduction**
This ER diagram models a **zoo management system**, focusing on the relationships between **Animals, Habitats, Keepers, and their assignments**. The system ensures that animals are properly housed, and keepers are assigned to maintain habitats efficiently.

---

## **2. Entities & Attributes**
### **Animal**
- **Primary Key:** `AnimalID`
- **Attributes:**
  - `Species` (**NOT NULL**) → Ensures each animal has a defined species.
  - `BirthDate` → Tracks the age of the animal.
  - `HealthStatus` (**DEFAULT "Healthy"**) → If not specified, animals are assumed to be in good health.
  - `HabitatID` (**Foreign Key**) → Ensures each animal belongs to a **valid habitat**.

- **Reasoning:**
  - The **foreign key `HabitatID`** links `Animal` to `Habitat`, enforcing that each animal must have a designated living area.
  - The **NOT NULL constraint** on `Species` prevents incomplete records.
  - The **DEFAULT "Healthy"** constraint ensures a valid default value when no health status is provided.

---

### **Habitat**
- **Primary Key:** `HabitatID`
- **Attributes:**
  - `Type` (**NOT NULL**) → Defines habitat type (e.g., "Savannah", "Aquarium").
  - `Capacity` (**CHECK `Capacity > 0`**) → Ensures a valid positive capacity.

- **Reasoning:**
  - The **CHECK constraint (`Capacity > 0`)** prevents invalid values (e.g., negative or zero capacity).
  - The **NOT NULL constraint** on `Type` ensures all habitats have a defined category.

---

### **Keeper**
- **Primary Key:** `KeeperID`
- **Attributes:**
  - `Name` (**VARCHAR(100) NOT NULL**) → Names cannot be empty.
  - `Specialty` (**VARCHAR(50) NOT NULL**) → Defines the area of expertise (e.g., Mammals, Birds).

- **Reasoning:**
  - **NOT NULL constraints** prevent missing information.
  - The `Specialty` attribute ensures that keepers are assigned to specific animal categories.

---

### **HabitatKeeper (Junction Table)**
- **Primary Key:** `(HabitatID, KeeperID)` (Composite Key)
- **Foreign Keys:**
  - `HabitatID` → References `Habitat(HabitatID)`.
  - `KeeperID` → References `Keeper(KeeperID)`.

- **Reasoning:**
  - **Many-to-Many Relationship**: A habitat can have **multiple keepers**, and a keeper can **manage multiple habitats**. The **junction table** resolves this.
  - The **composite primary key (`HabitatID`, `KeeperID`)** ensures that the same keeper cannot be assigned to the same habitat multiple times.
  - The **Foreign Keys (`HabitatID`, `KeeperID`)** enforce valid references to existing habitats and keepers.

---

## **3. Relationships & Constraints**
### **One-to-Many: `Habitat` → `Animal`**
- **Reasoning:** Each habitat can have **multiple animals**, but each animal is assigned to **only one habitat**.
- **Implementation:** The `HabitatID` in `Animal` is a **Foreign Key**.

### **Many-to-Many: `Keeper` ↔ `Habitat`**
- **Reasoning:** A **keeper** can manage multiple habitats, and a **habitat** can have multiple keepers.
- **Implementation:** `HabitatKeeper` serves as a **junction table**, with composite **Primary Key (`HabitatID`, `KeeperID`)**.

### **CHECK & DEFAULT Constraints**
- **CHECK (`Capacity > 0`)** prevents invalid data entry for habitat capacity.
- **DEFAULT `"Healthy"`** ensures a valid initial health status for new animals.

---

## **4. Summary**
This **ER model** ensures **data integrity**, **prevents invalid data**, and **optimizes relationships** between entities while enforcing necessary constraints. It supports **efficient zoo management**, ensuring **animals are housed properly**, and **keepers are assigned correctly**.

---