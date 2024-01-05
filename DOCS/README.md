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

```yaml
Project:
  Name: "E Commerce Platform"
  Description: "A platform to sell products"

  C_YourComponent:
    Template: "hub/tech_stack" # This will fetch a template for a specific tech stack,
    # a tech stack might be an express server or a react app or a flask server
    P_YourPart:
      Name: "What you call your part"
      Description: "What your part should do"
      Input:
        Type: "Object/String/Int"
        Description: "What your input is"
      Output:
        Type: "Object/String/Int"
        Description: "What your output is"
    GLUE:
      Code: "@/directory" # this is where your code for the specific tech stack will go
      # the route registration of anything else that interacts with the parts
      Description: "Glue code to hold together parts in the component"
      Dependencies: "..."
```


Once you have your definition written, you can put it into the root directory of your project (we will probably have an npm installer soon). You will be able to open the UI for either managing the project or just working on certain parts.






```
