/**
* Created: 2025/03/17
* 
* Updated: Apr 20 2025 with Bootstrap v5.3.3
* Author: Pascal Tene
* License: To be confirmed (Private)
*/

(function() {
    "use strict";
    $(document).ready(function() {
    //viewRequirementDetails();
    addCommentJson();
    /**
     * Easy selector helper function
     */
   
   function addComments(comment) {
    const commentsList = document.getElementById('commentsList');
    const comentItem = `
    <div class="card mb-3" id=" ${comment.comment_id} ">
        <div class="card-body">
            <h5 class="card-title">${comment.created_by}</h5>
            <p class="card-text" id="text{{comment.id}}"> ${comment.comment_text}</p>
            <small class="text-muted">${comment.created_date} </small>

            <!-- Reply, Update, and Delete Links -->
            <span href="#" class="comment-link reply-btn">Reply</span>
            {% if request.user == comment.created_by %}
                <a href="#" class="comment-link update-btn" data-comment-id="{{ comment.id }}" data-update-url="{% url 'update_comment' comment_id=comment.id %}">Update</a>
            {% endif %}
            {% if request.user == comment.created_by or request.user.is_superuser %}
                <a href="#" data-delete-url="{% url 'delete_comment' comment_id=comment.id %}" class="comment-link delete-btn">Delete</a>
            {% endif %}


            <!-- Reply Form -->
            <div class="reply-form" style="display: none; margin-top: 10px;">
                <form method="post" action="{% url 'add_reply' assetid=asset.id parent_id=comment.id %}">
                    {% csrf_token %}
                    <textarea name="comment_text" placeholder="Your repply comment.." required class="form-control" rows="4"></textarea>
                    <button type="submit" class="btn btn-success mt-3">Submit Reply</button>
                    
                </form>
            </div>
            {% if comment.replies.all %}
                <div class="mt-3 ms-4">
                    {% for reply in comment.replies.all %}
                        {% include 'comments/comment_item.html' with comment=reply %}
                    {% endfor %}
                </div>
            {% endif %}
        </div>
    </div>`;

    commentsList.innerHTML =  comentItem + commentsList.innerHTML;
   }

    function addCommentJson() {
       
        // Submit a new comment
        
        
        $('#comment-form-form').submit(function(e) {
            e.preventDefault();
            var form = $(this);
            var url = form.attr('action');
            var commentText = $('#comment-text').val();
            //$('#deleteCommentModal').modal('hide');

            $.ajax({
                url: url,
                type: 'POST',
                data: {
                    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                    'comment_text': commentText
                },
                success: function(response) {
                    if (response.success) {
                        
                       // $('#'+response.comment_id).remove();
                        //$('.ajax-alert').show()
                        //$('.alert-dismissible').show()
                        $('#ajax-alert-message').text("Comment added successfuly ");
                        console.log(response)
                        addComments(response); // Refresh the comments list
                      
                    } else {
                        alert('Error updating comment.');
                    }
                },
                error: function(response) {
                    alert('Error updating comment.');
                }
            });
        });
        

    }

});

  })();