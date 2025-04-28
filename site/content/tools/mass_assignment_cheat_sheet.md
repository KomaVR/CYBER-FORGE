---
title: "Mass_Assignment_Cheat_Sheet"
description: "
AutoBinding / Mass Assignment


Spring MVC

@ModelAttribute
會將 Client 端傳來的參數 (GET/POST) 綁定到指定 Object 中，並自動將此 Object 加到 ModelMap 中
Example

@RequestMapping(value = \"/home\", method = RequestMethod.GET)
    public String home(@ModelAttribute User user, Model model) {
        if (showSecret){
            model.addAttribute(\"firstSecret\", firstSecret);
        }
        return \"home\";
    }

Example 2:

justiceleague


Example 3: VolgaCTF 2019 - shop



"
url: "https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Mass_Assignment_Cheat_Sheet.md"
category: "Miscellaneous"
---
