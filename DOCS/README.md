# Ariad - Declarative Language

An Ariad project begins with the creation of a YAML document where you declare your project's structure and components. Writing YAML can be intricate, but with ChatGPT, you can easily articulate your project requirements and kickstart the YAML creation process.

Starting an Ariad project involves understanding its various components and how they interact within its unique architecture.

## Architecture

The architecture of Ariad is designed to be modular and flexible, enabling the independent development and integration of various components. Key concepts include Parts, GLUE, Components, and a Project Manager.

### Parts

Each 'Part' in Ariad represents a self-contained unit with specific inputs and outputs. Parts are designed to be developed independently, allowing for asynchronous and parallel development workflows.

### GLUE

'GLUE' acts as the linker within Ariad, connecting various Parts to form a cohesive Component. It defines how data flows from one Part to another and ensures that all Parts within a Component work in harmony.

### Components

A 'Component' in Ariad is a collection of Parts connected via GLUE. It takes an input, processes it through its constituent Parts, and then outputs the result. Components are the building blocks of an Ariad project, each serving a distinct function within the larger application.

### Project Manager

The Project Manager in Ariad oversees the overall structure of the program. It defines the necessary Parts, the GLUE that combines these parts, and how they fit into the broader project context.

### Templates

Components might follow certain templates, like an express backend server, providing a standardized approach to common functionalities within the project.

### Views

Ariad offers two primary views - the admin view and the working view. The admin view is for designing Components and the overall project, defining Parts and their interactions. The working view, akin to a leet-code-like interface, allows developers to select or be assigned Parts to code.

## Project Definition in YAML

Ariad projects are entirely declared in YAML. This includes defining the project's structure, Components, and their interactions. Here's an example of how a project can be declared:

1. The YAML file starts with the keyword `Project:` followed by the project details.
2. The project details include:
   - `Name:`: The name of the project.
   - `Description:`: A brief description of the project.
   - A list of components, each starting with a unique identifier like `C_Backend:` or `C_Frontend:`.
3. Each component has:
   - `Name:`: The name of the component.
   - `Description:`: A brief description of the component.
   - A list of parts, each starting with a unique identifier like `P_AddProduct:` or `P_GetProduct:`.
4. Each part has:
   - `Name:`: The name of the part.
   - `Description:`: A brief description of the part.
   - `Input:`: The input details, which include:
     - `Name:`: The name of the input.
     - `Type:`: The type of the input.
     - `Description:`: A brief description of the input.
     - `Properties:`: The properties of the input, each with a `Name:`, `Type:`, and `Description:`.
     - `Value:`: The value of the input.
   - `Output:`: The output details, similar to the input details.
5. Each component also has a `GLUE:` section that describes the flow of data between the parts. It includes:
   - `Graph:`: The flow of data, represented as `Part1 -> Part2`.
   - `Description:`: A brief description of the data flow.

Here's an example of a project definition in YAML:

```yaml
Project:
  Name: Pizza Project
  Description: A simple project with a cook and eater component
  C_Cook:
    Name: Pizza Maker
    Description: Handles the pizza making process
    P_MakePizza:
      Name: Make Pizza
      Description: Makes a pizza from given ingredients
      Input:
        Name: ingredients
        Type: Object
        Description: Object containing the details of the ingredients
        Properties:
          Dough:
            Type: String
            Description: Type of dough
          Sauce:
            Type: String
            Description: Type of sauce
          Toppings:
            Type: Array
            Description: Array of toppings
        Value: '{"Dough": "Thin crust", "Sauce": "Tomato", "Toppings": ["Cheese", "Pepperoni"]}'
      Output:
        Name: pizza
        Type: Object
        Description: Object containing the details of the pizza
        Properties:
          Dough:
            Type: String
            Description: Type of dough
          Sauce:
            Type: String
            Description: Type of sauce
          Toppings:
            Type: Array
            Description: Array of toppings
        Value: '{"Dough": "Thin crust", "Sauce": "Tomato", "Toppings": ["Cheese", "Pepperoni"]}'
    GLUE:
      Graph: P_MakePizza
      Description: Connects the pizza making process
  C_Eater:
    Name: Pizza Eater
    Description: Eats the pizza and gives feedback
    P_EatPizza:
      Name: Eat Pizza
      Description: Eats the pizza and gives an appreciation message
      Input:
        Name: pizza
        Type: Object
        Description: Object containing the details of the pizza
        Properties:
          Dough:
            Type: String
            Description: Type of dough
          Sauce:
            Type: String
            Description: Type of sauce
          Toppings:
            Type: Array
            Description: Array of toppings
        Value: '{"Dough": "Thin crust", "Sauce": "Tomato", "Toppings": ["Cheese", "Pepperoni"]}'
      Output:
        Name: appreciationMessage
        Type: String
        Description: Appreciation message after eating the pizza
        Value: "The pizza was delicious!"
    GLUE:
      Graph: P_EatPizza
      Description: Connects the pizza eating process
```

Some other examples can be found in the `examples` folder.
