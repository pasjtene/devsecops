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
    updateComment();
    //updateComment();
    /**
     * Easy selector helper function
     */
   
   function addNewComments(comment,deleteURL, updateURL,role) {
    const commentsList = document.getElementById('commentsList');
    const replyList = document.getElementById('replyCommentsList'+comment.parent_id);
    var uUrl = updateURL.replace("0",comment.comment_id);
    var dUrl = deleteURL.replace("0",comment.comment_id);

    const comentItem = `
    <div class="card mb-3" id="${comment.comment_id}">
        <div class="card-body">
            <h5 class="card-title">${comment.created_by}</h5>
            <p class="card-text" id="text${comment.comment_id}"> ${comment.comment_text}</p>
            <small class="text-muted">${new Date(comment.created_date).toLocaleString()} </small>

            <!-- Update, and Delete Links -->
                <span class="comment-link update-btn" 
                data-comment-id="${comment.comment_id}" data-update-url="${uUrl}">Update</span>
                <span data-delete-url="${dUrl}" class="comment-link delete-btn">Delete</span>
        </div>
    </div>`;

    if (role == "comment") {
        commentsList.innerHTML =  comentItem + commentsList.innerHTML;
    } else if (role == "reply") {
        
        replyList.innerHTML = comentItem + replyList.innerHTML;
        $(".reply-form").blur();
        $('.reply-form').hide();
        
    } else {
        console.log ('Role not known: ', role);
    }
    
    updateComment();
    //$('#text'+comment.comment_id).text(" ");
    $('#comment-text').val(' ');
   }

   function updateComment(){
     // Handle update comment modal
     $('.update-btn').click(function(e) {
        e.preventDefault();
        var commentId = $(this).data('comment-id');
        var updateUrl = $(this).data('update-url');
        //var updateUrl = "{% url 'update_comment' 0 %}".replace("0", commentId);
        var updtext = $(this).siblings('.card-text').text();
        $('#update-comment-text').val(updtext);

            $('#update-comment-form').attr('action', updateUrl);
            $('#updateCommentModal').modal('show');

    });

     // Handle delete comment modal
     $('.delete-btn').click(function(e) {
        e.preventDefault();
        var commentId = $(this).data('comment-id');
        var deleteUrl = $(this).data('delete-url');
        //var updateUrl = "{% url 'update_comment' 0 %}".replace("0", commentId);
        var deltext = $(this).siblings('.card-text').text();
        $('#delete-comment-text').val(deltext);

            $('#delete-comment-form').attr('action', deleteUrl);
            $('#deleteCommentModal').modal('show');

    });

    // Handle delete comment via AJAX
    $('#delete-comment-form').submit(function(e) {
        e.preventDefault();
        var form = $(this);
        var durl = form.attr('action');
        var commentText = $('#delete-comment-text').val();
        $('#deleteCommentModal').modal('hide');

        $.ajax({
            url: durl,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'comment_text': commentText
            },
            success: function(response) {
                if (response.success) {
                    console.log(response);
                    
                    $('#'+response.comment_id).remove();
                    $('.ajax-alert').show()
                    $('.alert-dismissible').show()
                    $('#ajax-alert-message').text("Comment deleted successfuly ");
                  
                } else {
                    console.log('Error Deleting comment.');
                    //alert('Error Deleting comment.');
                }
            },
            error: function(response) {
                //alert('Error deleting comment.');
                console.log('Error Deleting comment.');
            }
        });
    });
   }

    function addCommentJson() {
       
        // Submit a new comment
        $('.submit-comment-btn').click(function(e) {
            e.preventDefault();
            var url = $(this).closest(".comment-form-form").attr('action');
            var deleteURL = $(this).closest(".comment-form-form").data('delete-url');
            var updateURL = $(this).closest(".comment-form-form").data('update-url');
            var role = $(this).closest(".comment-form-form").data('role');
            var commentText = $(this).closest(".comment-form-form").find(".new-comment-text").val();
            $(this).closest(".comment-form-form").find(".new-comment-text").val("");
            
            //Remove focus from the text area before hiding it. This avoids browser errors.
            $(this).closest(".comment-form-form").find(".new-comment-text").blur();
            

            $.ajax({
                url: url,
                type: 'POST',
                data: {
                    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                    'comment_text': commentText
                },
                success: function(response) {
                    if (response.success) {
                        
                        $('#ajax-alert-message').text("Comment added successfuly ");
                        //The response is a comment. if the comment is a reply, then the parent_id is not null or None.
                        addNewComments(response,deleteURL,updateURL,role); // Refresh the comments list
                      
                    } else {
                       // alert('Error updating comment.');
                        console.log("No success")

                    }
                },
                error: function(response) {
                    //alert('Error updating comment.');
                    console.log("error: ",response);
                }
            });
        });

    }

});

  })();