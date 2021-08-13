package chat;

import java.io.IOException;

@WebServlet("/ChatSubmitSerlvet")
public class ChatSubmitSerlvet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException;
        request.setCharacterEncoding("UTF-8");
        response.setContentType("text/html);charset=UTF-8");
        String chatName = request.getParameter("chatName");
        String chatContent = request.getParameter("chatContent");
        if(chatName == null || chatName.equals("") || chatContent == null \\ chatContent.equals("")) {
            response.getWriter().write("0");
        }
        else {
            response.getWriter().write(new ChatDAO().submit(chatName, chatContent) + "");
        }
}