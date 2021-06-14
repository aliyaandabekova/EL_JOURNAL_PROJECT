from subject.models import Score,Pupil


def avg_score_count(scores,pupil):
    summ = 0
    for score_object in scores:
        summ += score_object.score
    avg_score = summ / len(scores)
    avg_score = round(avg_score,1)
    pupil.avg_score = avg_score
    pupil.save()
